from datetime import datetime, timedelta

from flask_pymongo import PyMongo
from flask import Flask
from testing_.kairos import Kairos

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://theiox:theioxsrvpwd@192.168.4.90:27017" + '/ilens_metadata'
mongo = PyMongo(app)
kairos = Kairos()

category_list = ['hour', 'hourly_target', 'day', 'shift', 'shifts_target', 'eoh', 'eod', 'eos','15min','30min']
for alarm_configuration in mongo.db.alarm_configuration.find(
        {"alarmType": "Alarm", "enabled": True,'isdeleted':{'$in':[False,'false']},"alarmCategory": {"$in": category_list}}, {"_id": 0}):
    print(alarm_configuration['alarmName'])
    # industry_data = mongo.db.industry.find_one({"industry_id": alarm_configuration['site_id']},
    #                                            {"_id": 0, "site_info.daystartsat": 1,"site_info.timezone": 1})
    # time_zone = industry_data.get('site_info').get('timezone')
    # print(time_zone)
    #
    # site_start_time = industry_data['site_info']['daystartsat']
    # site_start_hour = int(site_start_time.split(":")[0]) if site_start_time is not None and len(
    #     site_start_time.split(":")) <= 3 else 00
    # site_start_minute = int(site_start_time.split(":")[1]) if site_start_time is not None and len(
    #     site_start_time.split(":")) <= 3 else 00
    # site_start_second = int(site_start_time.split(":")[2]) if site_start_time is not None and len(
    #     site_start_time.split(":")) <= 3 else 00
    #
    # start_date_time = datetime.now().replace(hour=int(site_start_hour), minute=int(site_start_minute),
    #                                          second=int(site_start_second))
    # site_end_time = datetime.now()
    # # print(site_end_time)
    #
    # if start_date_time.replace(microsecond=00) > site_end_time.replace(microsecond=00):
    #     start = start_date_time - timedelta(days=1)
    # else:
    #     start = start_date_time
    #
    # # start_millisecond = get_millisecond_from_date_time(start.replace(microsecond=00), timezone=time_zone)
    # # end_millisecond = get_millisecond_from_date_time(site_end_time.replace(microsecond=00), timezone=time_zone)
    # print(start)