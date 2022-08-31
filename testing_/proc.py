from datetime import datetime

import traceback
from datetime import datetime, timedelta

import pytz
from flask import Flask
from flask_pymongo import PyMongo

from testing_.kairos import Kairos

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://theiox:theioxsrvpwd@192.168.4.90:27017" + '/ilens_metadata'
mongo = PyMongo(app)
app.config['MONGO_URI'] = "mongodb://theiox:theioxsrvpwd@192.168.4.90:27017" + '/ilens_events'
mongo_alarms_events = PyMongo(app)
kairos = Kairos()




def process_alarms_for_deltasum(device, val, alarmCategory, function, duration):
    try:
        start_time = end_time = datetime.now().replace(microsecond=0)
        for alarm_configuration in mongo.db.alarm_configuration.find(
                {"devices": device, "enabled": True, "isdeleted": False, 'alarmDuration':function, "alarmType": "Alarm",
                 "alarmCategory": alarmCategory}):
                condition=[]
                for configured_tag in alarm_configuration["ruleSets"][0]["rules"][:-1]:
                    
                    cond_ = tuple(map(lambda x: x['target_value'][alarmCategory][
                        duration] if alarmCategory == 'hourly_target' else x['target_value'][alarmCategory][
                        duration] if alarmCategory == 'shifts_target' else x['target_value'][alarmCategory][
                        duration] if alarmCategory == 'day_target' else configured_tag['rightHandSide'][
                        'customValue'], mongo.db.benchmark.find(
                        {"entity_id": {'$in': [device]}, "isdeleted": False, "function": "deltasum",
                         "entity_type": 'device_instance',
                         'tag_ids': {'$in': [j['leftHandSide']['tag'] for j in configured_tag]}})))[0]
                    
                    condition_satisfied = val.get(configured_tag['leftHandSide']['tag']) == cond_ if \
                        configured_tag["condition"] == "==" else (
                        val.get(configured_tag['leftHandSide']['tag']) != cond_ if configured_tag["condition"] == "!=" else (
                            val.get(configured_tag['leftHandSide']['tag']) >= cond_ if configured_tag["condition"] == ">=" else (
                                val.get(configured_tag['leftHandSide']['tag']) <= cond_ if configured_tag["condition"] == "<=" else (
                                    val.get(configured_tag['leftHandSide']['tag']) > cond_ if configured_tag["condition"] == ">" else (
                                        val.get(configured_tag['leftHandSide']['tag']) < cond_ if configured_tag["condition"] == "<" else False)))))
                    d=bool(configured_tag["operator"])
                    condition.extend([condition_satisfied, bool(configured_tag["operator"])])
                    customValue = cond_
                    if condition_satisfied:
                        generated_alarms_list = list(mongo_alarms_events.db.alarms.find(
                            {"alarm_id": alarm_configuration["id"], "device_instance_id": device,
                             "tag_id": configured_tag['leftHandSide']['tag'] ,  "is_reset": False}))
                        if len(generated_alarms_list) == 0:
                            device_name = ""
                            site_name = ""
                            tag_name = ""
                            priority_name = ""
                            priority_color = ""
                            priority_icon = ""

                            for alarm_event_unique_id in mongo.db.unique_id.find({"key": "alarm_event"}):
                                for device_instance in mongo.db.device_instance.find({"device_instance_id": device},
                                                                                     {"_id": 0}):
                                    device_name = device_instance["general_info"]["device_name"]
                                for industry in mongo.db.industry.find({"industry_id": alarm_configuration["site_id"]},
                                                                       {"_id": 0}):
                                    site_name = industry["industry_name"]
                                for tags in mongo.db.tag.find({"id": configured_tag['leftHandSide']['tag']}, {"_id": 0}):
                                    tag_name = tags["name"]
                                for priority_ in mongo.db.alarm_priority_type.find(
                                        {"id": alarm_configuration['priority']}, {"_id": 0}):
                                    priority_name = priority_["name"]
                                    priority_color = priority_["priorityColor"]
                                    priority_icon = priority_["icon"]
                                new_generated_template = alarm_configuration["alarmTemplate"].replace("[Device Name]",
                                                                                                      device_name)
                                new_generated_template = new_generated_template.replace("[Asset Name]", device_name)
                                new_generated_template = new_generated_template.replace("[Site Name]", site_name)
                                new_generated_template = new_generated_template.replace("[Tag Name]", tag_name)
                                new_generated_template = new_generated_template.replace("[Tag Value]",
                                                                                        str(round(val.get(configured_tag['leftHandSide']['tag']),
                                                                                                  2)) if abs(
                                                                                            val.get(configured_tag['leftHandSide']['tag'])) < 1000 else (
                                                                                                str(round(
                                                                                                    val.get(
                                                                                                        configured_tag[
                                                                                                            'leftHandSide'][
                                                                                                            'tag']) / 1000,
                                                                                                    2)) + " k"))
                                new_generated_template = new_generated_template.replace("[Time Stamp]", str(start_time))
                                new_generated_alarm = {
                                    "device_instance_id": device,
                                    "device_name": device_name,
                                    "alarm_id": alarm_configuration["id"],
                                    "site_id": alarm_configuration["site_id"],
                                    "client_id": alarm_configuration["client_id"],
                                    "tag_value": val.get(configured_tag['leftHandSide']['tag']),
                                    "start_time": start_time,
                                    "tag_name": tag_name,
                                    "id": "alarm_event_" + str(int(alarm_event_unique_id["id"]) + 1),
                                    "priority_id": alarm_configuration["priority"],
                                    "priority_name": priority_name if alarm_configuration["isTypeIsAlarm"] is True else "",
                                    "Priority_color": priority_color,
                                    "Priority_icon": priority_icon,
                                    "tag_id": configured_tag['leftHandSide']['tag'],
                                    "template": new_generated_template,
                                    "acknowledge": False,
                                    "acknowledge_time": "",
                                    "customValue": customValue,
                                    "alarmName": alarm_configuration["alarmName"],
                                    "alarmType": alarm_configuration["alarmType"],
                                    "alarmCategory": alarm_configuration['alarmCategory'],
                                    "alarmDuration": alarm_configuration["alarmDuration"],
                                    "associateTo": site_name,
                                    "is_reset": False,
                                    "reset_time": ""
                                }
                                mongo_alarms_events.db.alarms.insert(new_generated_alarm)
                                mongo.db.unique_id.update({"key": "alarm_event"},
                                                          {"$set": {"id": int(alarm_event_unique_id["id"]) + 1}})
                                # email_and_sms_generated_alarm(new_generated_alarm, alarm_configuration, block=alarm_configuration['levels'][0], level=0, device_id=device, tag_id=tag)
                    else:
                        for generated_alarm in mongo_alarms_events.db.alarms.find(
                                {"alarm_id": alarm_configuration["id"], "device_instance_id": device,
                                 "tag_id": configured_tag['leftHandSide']['tag'],  "is_reset": False}):
                            mongo_alarms_events.db.alarms.update({"id": generated_alarm["id"]},
                                                                 {"$set": {"is_reset": True, "reset_time": end_time}})
                        for triggered_alarm in mongo_alarms_events.db.triggered_alarms.find(
                                {"alarm_id": alarm_configuration["id"], "device_instance_id": device,
                                 "tag_id": configured_tag['leftHandSide']['tag'],  "is_reset": False}):
                            mongo_alarms_events.db.triggered_alarms.update({"id": triggered_alarm["id"]}, {
                                "$set": {"is_reset": True, "reset_time": end_time}})
    except Exception as e:
        traceback.print_exc()
        print(Exception)
