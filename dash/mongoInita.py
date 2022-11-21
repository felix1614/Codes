import time
from app_config import AppConfig
from collections import defaultdict
from pymongo import MongoClient, DESCENDING
from tzlocal import get_localzone

app_conf = AppConfig()

mongo = MongoClient(app_conf.get_mongo_uri('ilens_metadata'))
my_db = mongo['ilens_metadata']


class Config:
    def __init__(self):
        self.gateway_dict = {}
        self.instance_id_list = []
        self.sensor_collection = {}
        self.time_zone_dict = {}

    def mongo_query(self):
        for time_zone in my_db.industry.find({"isdeleted": {"$in": [False, "false"]}},{"site_info.timezone": 1,"industry_id":1, "_id": 0}, sort=[('_id', DESCENDING)]):
            self.time_zone_dict[time_zone["industry_id"]] = time_zone.get('site_info').get('timezone') if time_zone else str(get_localzone())

        st = time.time()
        for instance_id in my_db.gateway_instance.find({"isdeleted": {"$in": [False, "false"]},
                                                        "isdisabled": {"$in": [False, "false"]},
                                                        "type": "gateway_type_1"},
                                                       {"_id": 0, "gateway_instance_id": 1, "uniqueid":1}):
            if "uniqueid" in instance_id.keys():
                self.gateway_dict.update({instance_id["uniqueid"]:instance_id["gateway_instance_id"]})
                self.instance_id_list.append(instance_id["gateway_instance_id"])

        sensor_dict = defaultdict(dict)
        for _id in self.instance_id_list:
            sensor_dict[_id] = {}

            for data in my_db.sensor.find(
                    {"general_info.gateway_instance_id": _id,
                     'general_info.isdisabled': {"$in": ["false", False]},
                     'general_info.isdeleted': {"$in": ["false", False]}}, {'_id': 0}):
                sensor_dict[_id][data["general_info"]["device_com_id"]]= data

        self.sensor_collection = sensor_dict
        print("mongo fetch ", time.time() - st)
