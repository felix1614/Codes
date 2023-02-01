dict1 = {'key1': 50, 'key2': 100, 'key3': 300}
dict2 = {'key1': 50, 'key2': 100, 'key4': 400}

output = lambda di1, di2: {key: di1.get(key, 0) + di2.get(key, 0) for key in set(di1) | set(di2)}
dictSort = lambda dat: dict(sorted(dat.items(), key=lambda x: x[0]))
# print(output)
# output = OrderedDict()
# output.update(dict1)
#
# for key in dict1.keys() | dict2.keys():
#     output[key] = dict1.get(key, 0) + dict2.get(key, 0)
# from collections import ChainMap
# output = OrderedDict((key, dict1.get(key, 0) + dict2.get(key, 0)) for key in ChainMap(dict1, dict2))
# output = OrderedDict((key, dict1.get(key, 0) + dict2.get(key, 0)) for key in dict1.keys() | dict2.keys())
# output = OrderedDict((k, v) for k, v in output.items() if k in dict1 or k in dict2)
# output = OrderedDict((key, dict1.get(key, 0) + dict2.get(key, 0)) for key in dict1.keys() | dict2.keys())
# sorted_ = dict(sorted(output(dict1, dict2).items(), key=lambda x: x[0]))
sorted_ = dictSort(output(dict1, dict2))
print(sorted_)
