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

    def get_replica_set_name(self):
        return self.cfg['mongo_db']['replica_set_name']

    def get_schedule_mongo(self):
        s = self.cfg['mongo_db']['mongo_connection'].split(":")
        if self.cfg['mongo_db']['username'] and self.cfg['mongo_db']['password']:
            return True, s[0], int(s[1]), self.cfg['mongo_db']['username'], self.cfg['mongo_db']['password']
        else:
            return False, s[0], int(s[1]), None, None

    def get_kairos_host(self):
        return self.cfg['kairos_db']['url']

    def get_report_file_path(self):
        return self.cfg['service']['mnt_path']

    def get_kl_url(self):
        return self.cfg['service']['kl_url']

    def get_service(self):
        return self.cfg['service']

    def get_schedule(self):
        return self.cfg['scheduler']

    def get_mqtt_host(self):
        return self.cfg['mqtt']['host'], int(self.cfg['mqtt']['port'])

    def get_logs_path(self, path=None, level=None, ):
        if path:
            return self.cfg['log']['path']
        elif level:
            return self.cfg['log']['level']

    def get_meta_service_port(self):
        return self.cfg['service']['port']

    def get_environment(self):
        return self.cfg['environment']['mode']

    def get_token_expiry(self):
        return self.cfg["tokens_expiry"]

    def get_license_path(self):
        return self.cfg["service"]["license_path"]

    def get_sag_swell_tag(self):
        return self.cfg["sag_swell_interruption"]

    def get_plant_incomer_and_distribution_device_group(self):
        return self.cfg['plant_wise_energy_report']

    def get_plant_tags(self):
        return self.cfg['plant_wise_energy_report']['tags']

    def plant_report_mail_list(self):
        return  self.cfg['plant_wise_energy_report']['mail_list']

    def eb_incomer_and_dg_run_hour_tag(self):
        return  [self.cfg['plant_wise_energy_report']['eb_incomer']['tag_id'],self.cfg['plant_wise_energy_report']['dg_run_hours']['tag_id']]

    def get_eb_incomer_device_group_list(self):
        return self.cfg['plant_wise_energy_report']['eb_incomer']['device_group_id_list']

    def get_dg_run_hour_device(self):
        return self.cfg['plant_wise_energy_report']['dg_run_hours']['id']

    def get_plant_report_shift_timing(self):
        return self.cfg['plant_wise_energy_report']['shift_timings']

    def get_timezone(self):
        return self.cfg['timezone']['time_zone']

    def image_view(self):
        return self.cfg['image_view']['image_path']

    def table_row(self):
        return self.cfg["table_row_count"]["count"]
    def get_water_comsumption_tags_and_devices(self):
        return {'tags': self.cfg['plant_wise_energy_report']['tags']['water'], 'devices':self.cfg['plant_wise_energy_report']['water_information']}
    def get_egl_incomer_group(self):
        return self.cfg['EGL']['incomer_device_group']
    def get_bescom_power_consumption(self):
        return self.cfg['EGL']['bescom_power_consumption']
    def get_api(self):
        return self.cfg['api']['url']

    def get_iocl_devices(self):
        return self.cfg['IOCL']['devices']

    def get_iocl_tags(self):
        return self.cfg['IOCL']['tags']

    # def get_iocl_run_hr_devices(self):
    #     return self.cfg['IOCL']['screw_compressor_run_hours']

    def get_unit_conversion(self):
        return self.cfg['IOCL']['unit_conversion']

    def get_bottling_tags(self):
        return self.cfg['IOCL']['bottling_tags']

    def get_Specific_Energy_Consumption_deci(self):
        return self.cfg['IOCL']['decimal_point']

    def get_shift_tod_energy_report(self):
        return self.cfg['shift_tod_energy_report']['shifts']

    def get_dg_run_hour_tags(self):
        return self.cfg['DG_R_H']

    def get_api_limits(self):
        return self.cfg['rate_limits']

    def get_audit_log_schedule(self):
        return self.cfg['audit_log_scheduler']
