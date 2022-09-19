# # from pymongo import MongoClient
# import datetime
# import os
# import time
# from sys import argv
# # mongo_connection = "192.168.4.90:27017"
# # username = "theiox"
# # password = "theioxsrvpwd"
# # db_ = 'ilens_metadata'
# # mongo = MongoClient(f"mongodb://{username}:{password}@{mongo_connection}/{db_}")
# # my_db = mongo['ilens_metadata']
#
# # for i in my_db.benchmark.find({"client_id": "client_1", "site_id": "industry_10001_client_1", "created_by": "user_10068", "benchmark_id": "benchmark_86"}):
# # def wri(d):
# #     with open("/home/afnan/PycharmProjects/CodingManiac/shell_Scripting/hash_codes.csv", "a+") as f:
# #         f.write(f"{d}\n")
# #         f.close()
# # if not os.path.exists("/home/afnan/PycharmProjects/CodingManiac/shell_Scripting/hash_codes.csv"):
# #     with open("/home/afnan/PycharmProjects/CodingManiac/shell_Scripting/hash_codes.csv", "a+") as f:
# #         f.write(f"{argv[1]}\n")
# #         f.close()
# # wri("alarm_service,x.4.59,d50cf1622b077f4bfae97816fcfa5340d766ee703da7931802009f4702a254af")
# # wri("meta_service_2,x.0.54,d50cf1622b077f4bfae97816fcfa5340d766ee703da7931802009f4702a254afwew")
# # wri("meta_services_2,x.4.56,447a368f4c57197e8ed9fbe9f58915c9ff07688cc3e1b203593c03e50e96fb96")
# # wri("meta_services_2,x.0.45,dasd50cf1622b077f4bfae97816fcfa5340d766ee703da7931802009f4702a")
# # wri("alarm_service,x.0.65,d50cf1622b077f4bfae97816fcfa5340d766ee703da7931802009f4702a254af")
#
# ti= time.time()
# da = datetime.datetime.fromtimestamp(ti)
# print(da.strftime("%Y%m%d%H%M%S"))
# # ti = datetime.datetime.now()
# # cd =datetime.datetime.strftime(ti, '%d/%m/%y %H:%M:%S')
# # print(cd, datetime.datetime.strptime(cd, "%S"))
import pyodbc

# cnxn_str = ("Driver={ODBC Driver 17 for SQL Server};"
#             "Server=192.168.4.150;"
#             "Database=SAP_ELM;"
#             "UID=sa;"
#             "PWD=Elnetsrv123*;"
#             "Trusted_Connection=yes;")
# cnxn = pyodbc.connect(cnxn_str)
# cnxn = pyodbc.connect('DRIVER={SQL Server};'
#                       'SERVER=192.168.4.150;'
#                       'DATABASE=SAP_ELM;UID=saE;PWD=Elnetsrv123*;')
# import pyodbc

server = '192.168.4.150'
database = 'SAP_ELM'
username = 'sa'
password = 'Elnetsrv123*'
driver = "/etc/odbcinst.ini"

from sqlalchemy import create_engine
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)


