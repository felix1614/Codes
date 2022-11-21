# import json
from datetime import datetime
from itertools import islice

import pytz
from dateutil.parser import parse
from pymongo import MongoClient
from dash.kairos import Kairos
from dash.mongoInita import Config

kairos = Kairos()
mongo = f"mongodb://theiox:theioxsrvpwd@192.168.8.135:27018"
client = MongoClient(mongo)
# dataBase = Configs.getDatabase()
config = Config()
config.mongo_query()
db = client['ilens_metadata']
time_zone = config.time_zone_dict

with open("cmriData.out", "r") as reader:
    fileRead = reader.read().split("END")
    reader.close()

splitData = [i.replace("\n", "") for i in fileRead]
finalOut, loadVal, eventData, instantData, scalar = dict(), dict(), dict(), dict(), dict()
tuple(map(lambda x: finalOut.update({x.split(",")[0].lower(): x.split(",")[1:-1] if splitData.index(x) != len(splitData)-1 else x.split(",")[1:]}), splitData))

fields = ['category_1', 'category_2', 'category_3', 'category_4', 'category_5', 'category_6']
default = {"category_1": '', "category_2": '', "category_3": '', "category_4": '', "category_6": '', "category_7": '',
           "value": '', "previous_value": '', "last_visible": '', "timestamp": ''}
obiss = ['0100010600FF', '0100010601FF', '0100010602FF', '0100010603FF', '0100010604FF', '0100010605FF', '0100010606FF', '0100010607FF', '0100010608FF',
                         '0100090600FF', '0100090601FF', '0100090602FF', '0100090603FF', '0100090604FF', '0100090605FF', '0100090606FF', '0100090607FF', '0100090608FF']

def structure_query(raw_dict, site_id, gate_way_id, dev_ins_id, block, tag_list, sensor_id):
    gate_way_id, sensor_id = [gate_way_id] * len(tag_list), [sensor_id] * len(tag_list)
    site_id, block = [site_id] * len(tag_list), [f"block_{block}"] * len(tag_list)
    dev_ins_id = [dev_ins_id] * len(tag_list)
    result = list(zip(site_id, gate_way_id, dev_ins_id, block, tag_list, sensor_id))
    dicts = [dict(zip(fields, d)) for d in result]
    kairos_data_main = [{"name": "ilens.live_data.raw", "datapoints": [raw_val], 'tags': cat_dict} for raw_val, cat_dict
                        in zip(raw_dict, dicts)]
    return kairos_data_main


def splitter(arr, size):
    arr = iter(arr)
    return iter(lambda: tuple(islice(arr, size)), ())


for key in finalOut.copy().keys():
    notMap = ["RS485-Device_Address value".lower(), 'billing data value', 'instant data value', 'block load data value', 'daily load data value', 'billing load data value']
    
    if "value" in key and "event" not in key and key not in notMap and "scalar" not in key:
        OBIS = finalOut[key.replace("value", "obis")]
        keyVal = finalOut[key]
        finalOut[key] = dict(zip(OBIS, keyVal))
        del finalOut[key.replace("value", "obis")]
    
    elif "event" in key and "obis" not in key and "scalar" not in key:
        data_ = list(splitter(finalOut[key], len(finalOut[key.replace("value", "obis")])))
        eventData[key] = list(map(lambda x: {"obis": finalOut[key.replace("value", "obis")], "val": list(x)}, data_))
        del finalOut[key.replace("value", "obis")], finalOut[key]
    
    elif key in ['billing data value', 'daily load data value', 'block load data value']:
        load = list(map(list, list(splitter(finalOut[key], len(finalOut[key.replace("value", "obis")])))))
        # if key != 'billing data value':
        loadVal[key] = list(map(lambda x: {"obis": finalOut[key.replace("value", "obis")], "val": x}, load))
        # else:
        #     obisCode = finalOut[key.replace("value", "obis")]
        #     for obis in range(len(obisCode)):
        #         obiss = ['0100010600FF', '0100010601FF', '0100010602FF', '0100010603FF', '0100010604FF', '0100010605FF', '0100010606FF', '0100010607FF', '0100010608FF',
        #                  '0100090600FF', '0100090601FF', '0100090602FF', '0100090603FF', '0100090604FF', '0100090605FF', '0100090606FF', '0100090607FF', '0100090608FF']
        #         if obisCode[obis] in obiss:
                    # if obisCode[obis] not in scalar:
                    #     index = obis
                    #     for j in load:
                    #         df = j.pop(index)
                    #         sf = j.pop(index)
                    #         scalar[f"{obisCode[obis]}_{load.index(j)}"] = {"obis": f"{obisCode[obis]}", "time": sf, "val": df}
                    #     obisCode.remove(obisCode[obis])
                    #     obisCode.remove(obisCode[obis])

                        # scalar[]
                    # ef = obisCode.pop(indexx)
                    # hf = obisCode.pop(indexx)

        del finalOut[key.replace("value", "obis")], finalOut[key]
    
    elif key in ['instant data value']:
        load = list(splitter(finalOut[key], len(finalOut[key.replace("value", "obis")])))
        instantData[key] = list(map(lambda x: {"obis": finalOut[key.replace("value", "obis")], "val": list(x)}, load))
        # instantData[key] = {"obis": finalOut[key.replace("value", "obis")], "val": finalOut[key]}
        del finalOut[key.replace("value", "obis")], finalOut[key]
    
    elif "scalar" in key and "obis" in key:
        # OBIS = finalOut[key]
        # keyVal = finalOut[key.replace("obis", "value")]
        # scalar[key] = dict(zip(OBIS, keyVal))
        del finalOut[key.replace("obis", "value")], finalOut[key]


mainDict = {"GENERAL": finalOut, "EVENT": eventData, "LOAD": loadVal, "INSTANT": instantData, "SCALAR": scalar}
billing = mainDict["LOAD"]["billing data value"][0]
del eventData, loadVal, finalOut, instantData, scalar

# for i, j in mainDict.items():
#     if i == "LOAD":
#         for k, l in j.items():
#             if k == "billing data value":
#                 for obi_ in range(len(l)):
#                     for index in range(len(l[obi_]["obis"])):
#                         if l[obi_]["obis"][index] in [a'0100010600FF', '0100010601FF']:
#                             obiCode = l[obi_]["obis"][index]
#                             obiVal = l[obi_]["val"][index]
#                             if "MAXIMUM" not in mainDict.keys():
#                                 mainDict["MAXIMUM"] = {obiCode: {"val": obiVal}}
#                             else:
#                                 mainDict["MAXIMUM"][obiCode]["time"] = obiVal


def get_millisecond_from_date_time(date_time, industry_zone):
    tz = pytz.timezone(industry_zone)
    dt_with_tz = tz.localize(date_time, is_dst=None)
    seconds = (dt_with_tz - datetime(1970, 1, 1, tzinfo=pytz.UTC)).total_seconds()
    return seconds * 1000


def processData(cmriVal=None, obi=None, industryId=None, tagId=None, gateWay=None, devId=None, sensId=None, block=None):
    val, tags = [], []

    def is_date(string, fuzzy=False):
        try:
            parse(string, fuzzy=fuzzy)
            return True
        except ValueError:
            return False

    for Key_, Val_ in cmriVal.items():
        # if Key_ not in ['billing data value']:
        for vals in Val_:
            vals["obis"] = vals["obis"]
            payload_time = vals["val"][0]
            payload_time = datetime.strptime(payload_time, '%d/%m/%Y %H:%M:%S')
            timestamp = get_millisecond_from_date_time(payload_time, time_zone[industryId])
            for obiIds in range(len(obi)):
                if obi[obiIds] in vals["obis"]:
                    if obi[obiIds] not in obiss:
                        value = vals["val"][vals["obis"].index(obi[obiIds])]
                        if not is_date(value):
                            tags += tagId[obiIds],
                            val += [timestamp, eval(value)],

                    else:
                        value = vals["val"][vals["obis"].index(obi[obiIds])]
                        timeStamp = vals["val"][vals["obis"].index(obi[obiIds])+1]
                        tags += tagId[obiIds],
                        time_ = datetime.strptime(timeStamp, '%d/%m/%Y %H:%M:%S')
                        timestamp = get_millisecond_from_date_time(time_, time_zone[industryId])
                        val += [timestamp, eval(value)]
            kaiData = structure_query(val, industryId, gateWay, devId, block, tags, sensId)
            kairos.update_kairos_data(True, kaiData)
            print(f"{Key_} data inserted for {payload_time}")
        # else:
        #     for vals in Val_:
        #         vals["obis"] = vals["obis"]
        #         payload_time = vals["val"][0]
        #         payload_time = datetime.strptime(payload_time, '%d/%m/%Y %H:%M:%S')
        #         timestamp = get_millisecond_from_date_time(payload_time, time_zone[industryId])
        #         # max_obis, max_tag, max_val = [], [], []
        #         for obiIds in range(len(obi)):
        #             if obi[obiIds] in vals["obis"]:
        #                 if obi[obiIds] not in obiss:
        #                     value = vals["val"][vals["obis"].index(obi[obiIds])]
        #                     if not is_date(value):
        #                         tags += tagId[obiIds],
        #                         val += [timestamp, value],
        #                 else:
        #                     value = vals["val"][vals["obis"].index(obi[obiIds])]
        #                     timeStamp = vals["val"][vals["obis"].index(obi[obiIds])+1]
        #                     tags += tagId[obiIds],
        #                     val += [timeStamp, value]
        #         kaiData = structure_query(val, industryId, gateWay, devId, block, tags, sensId)
        #         kairos.update_kairos_data(True, kaiData)
        #         print(f"{Key_} data inserted for {payload_time}")


def kairStore(obi=None, tagId=None, block=None, industryId=None, gateWay=None, devId=None, sensId=None):
    for cmriKey, cmriVal in mainDict.items():
        if cmriKey == 'GENERAL':
            pass
        elif cmriKey == 'EVENT':
            processData(cmriVal=cmriVal, obi=obi, industryId=industryId, tagId=tagId, gateWay=gateWay, devId=devId,
                        sensId=sensId, block=block)
            print(f"Event data inserted for block: {block}")
            # for eventKey, eventVal in cmriVal.items():
            #     for vals in eventVal:
            #         vals["obis"] = vals["obis"][1:]
            #         payload_time = vals["val"].pop(0)
            #         payload_time = datetime.strptime(payload_time, '%d/%m/%Y %H:%M:%S')
            #         timestamp = get_millisecond_from_date_time(payload_time, time_zone[industryId])
            #         for obiIds in range(len(obi)):
            #             if obi[obiIds] in vals["obis"]:
            #                 tags += tagId[obiIds],
            #                 val += [timestamp, vals["val"][vals["obis"].index(obi[obiIds])]],
            #         kaiData = structure_query(val, industryId, gateWay, devId, block, tags, sensId)
            #         kairos.update_kairos_data(True, kaiData)
            #         print("data inserted")

        elif cmriKey == 'LOAD':
            processData(cmriVal=cmriVal, obi=obi, industryId=industryId, tagId=tagId, gateWay=gateWay, devId=devId, sensId=sensId, block=block)
            print(f"Load data inserted for block {block}")

        elif cmriKey == 'INSTANT':
            processData(cmriVal=cmriVal, obi=obi, industryId=industryId, tagId=tagId, gateWay=gateWay, devId=devId,
                        sensId=sensId, block=block)
            print(f"Instant data inserted for block {block}")


# daily = obisToTags(mainDict["LOAD"]["daily load data value"][0]['obis'])
sensor = "sensor_10123"
tagIds = []
obis_ = []
virtualDev = []
obis = [i for i in db.obis_tags.find({})]
for sen in db.sensor.find({"device_instance_id": sensor}):
    for block_ in sen['deviceConfig']:
        tuple(map(lambda tag: (obis_.append(obis[0][tag["tag_id"]]["obis"]), tagIds.append(tag["tag_id"]), virtualDev.append(tag["device_instance_id"]) if tag["device_instance_id"] not in virtualDev else "") if f"{tag['tag_id']}" in obis[0].keys() else "", block_['tagsData']))
        tagIds = ' '.join(tagIds).split()
        obis_ = ' '.join(obis_).split()
        virtualDev = ' '.join(virtualDev).split()
        tuple(map(lambda virtual: kairStore(obi=obis_, tagId=tagIds, block=block_["blockNumber"], industryId=sen['site_id'], gateWay=sen['general_info']['gateway_instance_id'], devId=virtual, sensId=sen["device_instance_id"]), virtualDev))
        # for tag in block['tagsData']:
        #     if f"{tag['tag_id']}" in obis[0].keys():
        #         obis_ += obis[0][tag["tag_id"]]["obis"],
        #         tagIds += tag["tag_id"],
            # obis_ += "".join([d["id"] for d in obis if d["belongs_to"] == f"{tag['tag_id']}"]),
            # tagIds += "".join([d["belongs_to"] for d in obis if d["belongs_to"] == f"{tag['tag_id']}"]),

