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

    def get_kairos_host(self):
        return self.cfg['kairos_db']['url']

    def get_mqtt_host(self):
        return self.cfg['mqtt']['host'], int(self.cfg['mqtt']['port']), self.cfg['mqtt']['topic'], self.cfg['mqtt']['data_acq_topic']

    def get_web_socket_host(self):
        return self.cfg['mqtt_web_socket']['host'], int(self.cfg['mqtt_web_socket']['port'])

    def web_ssl(self):
        return self.cfg['mqtt_web_socket']['ssl'], self.cfg['mqtt_web_socket']['cert_path']

    def get_logs_path(self, path=None, level=None, retention=None, rotation=None):
        if path:
            return self.cfg['log']['path']
        elif level:
            return self.cfg['log']['level']
        elif retention:
            return self.cfg['log']['retention']
        elif rotation:
            return self.cfg['log']['rotation']

    def get_rotaion_retention(self, rotation=None, retention=None, ):
        if rotation:
            return self.cfg['log']['rotation']
        elif retention:
            return self.cfg['log']['retention']

    def get_audit_log_schedule(self):
        return self.cfg['audit_log_scheduler']
