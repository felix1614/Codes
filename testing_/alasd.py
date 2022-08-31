import traceback
from datetime import datetime

import pytz
from flask import Flask
from flask_pymongo import PyMongo

from testing_.kairos import Kairos
from testing_.proc import process_alarms_for_deltasum

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://theiox:theioxsrvpwd@192.168.8.135:27018" + '/ilens_metadata'
mongo = PyMongo(app)
kairos = Kairos()

def get_millisecond_from_date_time(date_time, timezone):
    try:
        tz = pytz.timezone(timezone)
        dt_with_tz = tz.localize(date_time, is_dst=None)
        seconds = (dt_with_tz - datetime(1970, 1, 1, tzinfo=pytz.UTC)).total_seconds()
        return seconds * 1000
    except Exception as e:
        traceback.print_exc()



def deltasum(start_millisecond, end_millisecond, duration, triger_time = None, timings= None):
    try:
        for alarm_configuration in mongo.db.alarm_configuration.find(
                {"alarmType": "Alarm", "alarmDuration": "deltasum",'alarmCategory':duration, "enabled": True, "isdeleted": False}, {"_id": 0}):
            for devices in alarm_configuration["devices"]:
                delta = {}
                for rule in alarm_configuration["ruleSets"][0]["rules"]:
                    kairos.set_metrics_name("ilens.live_data.raw")
                    kairos.set_metrics_tags(
                        {
                            "category_3": [devices],
                            "category_5": [rule["leftHandSide"]["tag"]]
                        }
                    )
                    kairos.set_start_end_date(True, start_millisecond, end_millisecond)
                    kairos.set_metrics_aggregators([
                        {
                            "name": "filter",
                            "filter_op": "lte",
                            "threshold": "0"
                        },
                        {
                            "name": "first",
                            "sampling": {
                                "value": "1",
                                "unit": "minutes"
                            },
                            "align_start_time": True
                        },
                        {
                            "name": "diff"
                        },
                        {
                            "name": "filter",
                            "filter_op": "lte",
                            "threshold": "0"
                        },
                        {
                            "name": "sum",
                            "sampling": {
                                "value": "1",
                                "unit": "days"
                            }
                        }
                    ])
                    response = kairos.get_kairos_data()
                    deltasum_value = None
                    for values in response:
                        value = values["values"]
                        if len(value) == 0:
                            deltasum_value = 0
                        else:
                            deltasum_value = value[0][1]

                    delta[rule["leftHandSide"]["tag"]]=deltasum_value


                if alarm_configuration['alarmCategory'] == "hour":
                    process_alarms_for_deltasum(devices, delta,
                                                alarm_configuration['alarmCategory'], alarm_configuration['alarmDuration'], duration)

                elif alarm_configuration['alarmCategory'] == "hourly_target":
                    process_alarms_for_deltasum(devices, delta,
                                                alarm_configuration['alarmCategory'],alarm_configuration['alarmDuration'], timings)

                elif alarm_configuration['alarmCategory'] == "day":
                    process_alarms_for_deltasum(devices, delta,
                                                alarm_configuration['alarmCategory'],alarm_configuration['alarmDuration'], duration)
                elif alarm_configuration['alarmCategory'] == "day_target":
                    process_alarms_for_deltasum(devices,  delta,
                                                alarm_configuration['alarmCategory'],alarm_configuration['alarmDuration'], timings)

                elif alarm_configuration['alarmCategory'] == "shift":
                    process_alarms_for_deltasum(devices, delta,
                                                alarm_configuration['alarmCategory'],alarm_configuration['alarmDuration'], duration)

                elif alarm_configuration['alarmCategory'] == "shift_target":
                    process_alarms_for_deltasum(devices, delta,
                                                alarm_configuration['alarmCategory'],alarm_configuration['alarmDuration'], timings)


    except Exception as e:
        traceback.print_exc()


category_list = ['hour', 'day', 'shift', 'eoh', 'eod', 'eos','15min','30min']
for alarm_configuration in mongo.db.alarm_configuration.find(
        {"alarmType": "Alarm", "enabled": True,'isdeleted':{'$in':[False,'false']},"alarmCategory": {"$in": category_list}}, {"_id": 0}):
    industry_data = mongo.db.industry.find_one({"industry_id": alarm_configuration['site_id']},
                                               {"_id": 0, "site_info.daystartsat": 1,"site_info.timezone": 1})
    time_zone = industry_data.get('site_info').get('timezone')

    if alarm_configuration['alarmCategory'] !='hour':
        continue

    if alarm_configuration['alarmCategory'] == "hour":
        start_date = datetime.now().strftime("%H:%M:%S")
        site_start_hour = int(start_date.split(":")[0]) if start_date is not None and len(
            start_date.split(":")) <= 3 else 00
        site_start_minute = 00
        site_start_second = 00
        start_date_time = datetime.now().replace(hour=int(site_start_hour), minute=int(site_start_minute),
                                                 second=int(site_start_second))
        end_time = datetime.now()

        start_millisecond = get_millisecond_from_date_time(start_date_time.replace(microsecond=00),timezone=time_zone)
        end_millisecond = get_millisecond_from_date_time(end_time.replace(microsecond=00),timezone=time_zone)
        if alarm_configuration['alarmDuration'] == "deltasum":
            deltasum(start_millisecond, end_millisecond, alarm_configuration['alarmCategory'], timings = start_date_time.strftime("%H"))
