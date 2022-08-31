import yaml


class AppConfig:
    def __init__(self):
        config_path = "config.yml"
        with open(config_path, 'r') as ymlFile:
            self.cfg = yaml.load(ymlFile, Loader=yaml.FullLoader)

    def get_mongo_host(self):
        if self.cfg['mongo_db']['username'] and self.cfg['mongo_db']['password']:
            return f"mongodb://{self.cfg['mongo_db']['username']}:{self.cfg['mongo_db']['password']}@{self.cfg['mongo_db']['mongo_connection']}"
        else:
            return f"mongodb://{self.cfg['mongo_db']['mongo_connection']}"

    def get_mongo_uri(self, db_name):
        if self.cfg['mongo_db']['username'] and self.cfg['mongo_db']['password']:
            return f"mongodb://{self.cfg['mongo_db']['username']}:{self.cfg['mongo_db']['password']}@{self.cfg['mongo_db']['mongo_connection']}/{db_name}"
        else:
            return f"mongodb://{self.cfg['mongo_db']['mongo_connection']}/{db_name}"

    def get_environment(self):
        return self.cfg['environment']['mode']

    def get_mqtt_details(self):
        return self.cfg['mqtt_broker']

    def get_license_path(self):
        return self.cfg["service"]["license_path"]

    def get_kairos_host(self):
        return self.cfg['kairos_db']['url']

    def get_duration(self):
        return self.cfg['duration']["timer"]

    def get_timezone(self):
        return self.cfg['timezone']['timezone']

    def get_alarm_sms_count(self):
        return self.cfg['sms_count']

    def get_logs_path(self, path=None, level=None, ):
        if path:
            return self.cfg['log']['path']
        elif level:
            return self.cfg['log']['level']
    def get_rotaion_retention(self, rotation=None, retention=None, ):
        if rotation:
            return self.cfg['log']['rotation']
        elif retention:
            return self.cfg['log']['retention']