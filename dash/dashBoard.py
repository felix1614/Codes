from itertools import islice

# splitData = []
with open("cmriData.out", "r") as reader:
    fileRead = reader.read().split("END")
reader.close()
# tuple(map(lambda dat: splitData.append(dat.replace("\n", "")), fileRead))
splitData = [i.replace("\n", "") for i in fileRead]
finalOut, mainDict, loadVal, eventData, instantData, scalar = dict(), dict(), dict(), dict(), dict(), dict()
# finalOut = map(lambda x: {x.split(",")[0].lower(): x.split(",")[1:-1] if splitData.index(x) != len(splitData)-1 else x.split(",")[1:]}, splitData)
tuple(map(lambda x: finalOut.update({x.split(",")[0].lower(): x.split(",")[1:-1] if splitData.index(x) != len(splitData)-1 else x.split(",")[1:]}), splitData))

# for da in finalOut.keys():
#     if "obis" in da and da.replace("data", "scalar") in da and da != "event scalar obis":
#         for obi in range(len(finalOut[da])):
#             if finalOut[da][obi] in finalOut[da.replace("data", "scalar")]:
#                 index = finalOut[da][obi]
#                 finalOut[da.replace("scalar", "data")][obi] = f"{index}_{'scalar'}"
#                 # finalOut[da.replace("data", "scalar")].pop(finalOut[da.replace("data", "scalar")].index(finalOut[da][obi]))
#                 print(finalOut[da][obi])
#                 # del finalOut[da.replace("data", "scalar")][]
#                 # obi = finalOut[da.replace("data", "scalar")][]


def chunk(arr, size):
    arr = iter(arr)
    return iter(lambda: tuple(islice(arr, size)), ())


for key in finalOut.copy().keys():
    # notMap = ["RS485-Device_Address value".lower(), 'billing data value', 'instant data value', 'instant data value'.replace("data", "scalar"), 'billing data value'.replace("data", "scalar"), 'block load data value', 'block load data value'.replace("data", "scalar"), 'daily load data value', 'daily load data value'.replace("data", "scalar"), 'billing load data value', 'billing load data value'.replace("data", "scalar")]
    notMap = ["RS485-Device_Address value".lower(), 'billing data value', 'instant data value', 'block load data value', 'daily load data value', 'billing load data value']
    if "value" in key and "event" not in key and key not in notMap and "scalar" not in key:
        OBIS = finalOut[key.replace("value", "obis")]
        keyVal = finalOut[key]
        finalOut[key] = dict(zip(OBIS, keyVal))
        # finalOut[key] = {"obis": OBIS, "val": keyVal}
        del finalOut[key.replace("value", "obis")]
    elif "event" in key and "obis" not in key and "scalar" not in key:
        # eventData[key] = {"obis": finalOut[key.replace("value", "obis")], "value": finalOut[key]}
        data_ = list(chunk(finalOut[key], len(finalOut[key.replace("value", "obis")])))
        # eventData[key] = list(map(lambda x: dict(zip(finalOut[key.replace("value", "obis")], x)), data_)),
        eventData[key] = list(map(lambda x: {"obis": finalOut[key.replace("value", "obis")], "val": x}, data_))
        del finalOut[key.replace("value", "obis")], finalOut[key]
    elif key in ['billing data value', 'daily load data value', 'block load data value']:
        # data_ = list(chunk(finalOut[key], len(finalOut[key.replace("value", "obis")])))
        # keyIn = key.replace("data", "scalar")
        # loadVal[key] = list(map(lambda x: dict(zip(finalOut[keyIn], x)), data_)),
        # loadVal[key] = {"obis": finalOut[key.replace("value", "obis")], "value": finalOut[key]}
        load = list(chunk(finalOut[key], len(finalOut[key.replace("value", "obis")])))
        # scalar = key.replace("data", "scalar")
        # scalar = scalar.replace("value", "obis")
        # loadVal[key] = list(map(lambda x: {"obis": finalOut[key.replace("value", "obis")], "val": x, "scalar": finalOut[scalar]}, load))
        # loadVal[key] = list(map(lambda x: {"obis": finalOut[key.replace("value", "obis")], "val": x}, load))

        # loadVal[key] = list(map(lambda x: {"obis": finalOut[key.replace("value", "obis")], "val": x}, load))
        loadVal[key] = list(map(lambda x: dict(map(lambda key_, val_: (key_, val_), finalOut[key.replace("value", "obis")], x)), load))
        # loadVal[key] = list(map(lambda x: {k[i]: x[i] for i in range(len(k))}, load))

        del finalOut[key.replace("value", "obis")], finalOut[key]
    elif key in ['instant data value']:
        load = list(chunk(finalOut[key], len(finalOut[key.replace("value", "obis")])))
        # scalar = key.replace("data", "scalar")
        # scalar = scalar.replace("value", "obis")
        # instantData[key] = {"obis": finalOut[key.replace("value", "obis")], "val": load, "scalar": finalOut[scalar]}
        instantData[key] = {"obis": finalOut[key.replace("value", "obis")], "val": finalOut[key]}
        del finalOut[key.replace("value", "obis")], finalOut[key]
    elif "scalar" in key and "obis" in key:
        OBIS = finalOut[key]
        keyVal = finalOut[key.replace("obis", "value")]
        scalar[key] = dict(zip(OBIS, keyVal))
        # finalOut[key] = {"obis": OBIS, "val": keyVal}
        del finalOut[key.replace("obis", "value")], finalOut[key]

print(finalOut)
mainDict = {"actualData": finalOut, "eventData": eventData, "loadData": loadVal, "instantData": instantData, "scalar": scalar}
del eventData, loadVal, finalOut, instantData, scalar


sdfsf = mainDict




