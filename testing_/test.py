import os
import traceback
from datetime import datetime
from pathlib import Path

import pytz
from flask import Flask
from flask_pymongo import PyMongo

from testing_.kairos import Kairos

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://theiox:theioxsrvpwd@192.168.8.135:27018" + '/ilens_metadata'
mongo = PyMongo(app)
kairos = Kairos()

as_="device_instance_10007"
alarmCategory='hourly_target'
shift="Shift 1"
day='2022/6/15'
# alarm_configuration = tuple(map(lambda x: x, mongo.db.alarm_configuration.find({"devices": as_, "enabled": True, "isdeleted": False, "alarmDuration": "deltasum", "alarmType": "Alarm", "alarmCategory": alarmCategory})))[0]
# cd=list(set([i["operator"] if "operator" in i.keys() else "or" for i in alarm_configuration["ruleSets"][0]["rules"]]))
# print(cd)
# if "and" in cd:
#     print("pass")
# else:
#     print("sum")

# configured_tag=alarm_configuration.get('ruleSets')[0]['rules']



asas=eval(' '.join(["False","and","True",'']))
# print(asas)

# for configure_tag in (alarm_configuration["ruleSets"][0]["rules"])[::-1]:
#     da=configure_tag
#     print(configure_tag)


# d=[]
# for i in range(len(configured_tag)):
#     cond_ = tuple(map(lambda x: x['target_value'][alarmCategory][datetime.now().strftime("%H")] if alarmCategory=='hourly_target' else x['target_value'][alarmCategory]['shift_1'] if alarmCategory=='shifts_target' else x['target_value'][alarmCategory][day] if alarmCategory=='day_target' else configured_tag[i]['rightHandSide']['customValue'], mongo.db.benchmark.find({"entity_id": {'$in': [as_]}, "isdeleted": False, "function": "deltasum", "entity_type": 'device_instance', 'tag_ids': {'$in': [i['leftHandSide']['tag'] for i in configured_tag]}})))[0]
#     condition_satisfied = 0 == cond_ if configured_tag[i].get('condition') == "==" else (
#         0 != cond_ if configured_tag[i].get('condition') == "!=" else (
#             0 >= cond_ if configured_tag[i].get('condition') == ">=" else (
#                 0 <= cond_ if configured_tag[i].get('condition') == "<=" else (
#                     0 > cond_ if configured_tag[i].get('condition') == ">" else (
#                         0 < cond_ if configured_tag[i].get('condition') == "<" else False)))))
#     d.extend([condition_satisfied, configured_tag[i].get('operator')])
#
# print(bool(d))
#
#
#
#










#         if i+1 < len(configured_tag) and alarmCategory in ['hourly_target', 'shifts_target', 'day_target']:
#             cond_2 = tuple(map(lambda x: x['target_value'][alarmCategory][datetime.now().strftime("%H")] if alarmCategory=='hourly_target' else x['target_value'][alarmCategory]['shift_1'] if alarmCategory=='shifts_target' else x['target_value'][alarmCategory][day] if alarmCategory=='day_target' else configured_tag[i+1]['rightHandSide']['customValue'], mongo.db.benchmark.find({"entity_id": {'$in': [as_]}, "isdeleted": False, "function": "deltasum", "entity_type": 'device_instance', 'tag_ids': {'$in': [i['leftHandSide']['tag'] for i in configured_tag]}})))[0]
#             condition_satisfied_2 = 0 == cond_2 if configured_tag[i+1].get(
#                 'condition') == "==" else (
#                 0 != cond_2 if configured_tag[i+1].get('condition') == "!=" else (
#                     0 >= cond_2 if configured_tag[i+1].get('condition') == ">=" else (
#                         0 <= cond_2 if configured_tag[i+1].get('condition') == "<=" else (
#                             0 > cond_2 if configured_tag[i+1].get('condition') == ">" else (
#                                 0 < cond_2 if configured_tag[i+1].get(
#                                     'condition') == "<" else False)))))
#     if i == len(configured_tag)-1 or alarmCategory not in ['hourly_target', 'shifts_target', 'day_target']:
#         condition_satisfied_2 = condition_satisfied_1
#
#     if configured_tag[i].get('operator') =='and' and alarmCategory in ['hourly_target', 'shifts_target', 'day_target']:
#         condition_satisfied = condition_satisfied_1 and condition_satisfied_2
#         custom_value = cond_
#         print(custom_value)
#         # print(condition_satisfied)
#     elif configured_tag[i].get('operator') =='or' and alarmCategory in ['hourly_target', 'shifts_target', 'day_target']:
#         condition_satisfied = condition_satisfied_1 or condition_satisfied_2
#         custom_value = cond_
#         print(custom_value)
#         # print(condition_satisfied)
#     print(condition_satisfied)
#     if condition_satisfied:
#         print("success")
#
# # da = []
# ca = []
# for alarm_configuration in mongo.db.alarm_configuration.find(
#         {"alarmType": "Alarm", "alarmDuration": "deltasum", 'alarmCategory': 'hour', "enabled": True,
#          "isdeleted": False}, {"_id": 0}):
#     for devices in alarm_configuration["devices"]:
#         conf = alarm_configuration["ruleSets"][0]["rules"]
#         for rule in range(len(conf)):
#             ca.append(conf[rule]["leftHandSide"]["tag"])
#             if rule==len(conf)-1:
#                 print(conf[rule]["leftHandSide"]["tag"])
#             elif rule+1 < len(conf):
#                 da.append(conf[rule+1]["leftHandSide"]["tag"])
# print(ca)
# print(da)


