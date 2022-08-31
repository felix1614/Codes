#!/bin/bash

PYCMD=$(cat <<EOF
import os
import traceback
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys
import yaml
from pymongo import MongoClient

class AppConfig:
    def __init__(self):
        config_path = "config.yml"
        with open(config_path, 'r') as ymlFile:
            self.cfg = yaml.load(ymlFile, Loader=yaml.FullLoader)

#    def log_path(self):
#        return self.cfg['logging']['log']

    def finalPath(self):
        return self.cfg['logging']['final']

    def file_size(self):
        return self.cfg['fileSize']

    def siteEmails(self):
        return self.cfg['siteEmails']

    def serverDetails(self):
        return self.cfg['mailServerCred']


app_conf = AppConfig()

def send_mail(toAddr, PATH, frmAddr, passWord):
    try:
        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        msg = MIMEMultipart()
        msg['From'], msg['To'] = frmAddr, toAddr
        msg['Subject'] = "Rejected pkts"
        msg.attach(MIMEText("kindly find the attached file of the rejected pkts", 'plain'))
        fileName = "rejected_packets.tar.gz"
        if not os.path.exists(f"{PATH}rejected_packets.tar.gz"):
            os.system(f"tar -cvzf {PATH}{fileName} {PATH}rejected_pkt/")
        if os.path.exists(f"{PATH}rejected_packets.tar.gz"):
            attachment = open(f"{PATH}rejected_packets.tar.gz", "rb")
            p = MIMEBase('application', 'octet-stream')
            p.set_payload(attachment.read()), encoders.encode_base64(p)
            p.add_header('Content-Disposition', "attachment; filename= %s" % fileName)
            msg.attach(p)
            mailServer.starttls()
            mailServer.login(frmAddr, passWord)
            txt = msg.as_string()
            mailServer.send_message(msg)
            mailServer.quit()
            print(f"mail has been sent to {toAddr}")

    except Exception as e:
        traceback.print_exc()

if os.path.exists(f"{app_conf.finalPath()}rejected_pkt") and os.path.getsize(f"{app_conf.finalPath()}rejected_pkt") >= 4096:
    serverCred = app_conf.serverDetails()
    send_mail(', '.join(app_conf.siteEmails()), app_conf.finalPath(), serverCred[0], serverCred[1])
    name = "".join(os.popen("w -h -s | cut -c1-9").read().split())  # gets the logged in account userName
    centralizedDir = f"/home/{name}/RejectedPackets/{'modServer'}/"
    print(centralizedDir)
    if not os.path.exists(centralizedDir):
        os.system(f"mkdir -p {centralizedDir}")
        print("directory created")
    os.system(f"mv {app_conf.finalPath()}rejected_pkt/*  {centralizedDir}")
    os.system(f"rm {app_conf.finalPath()}/rejected_packets.tar.gz")

EOF
)
#LIB=$(pip3 list | grep PyYAML)
#if [ ${#LIB} == 0 ];then
#  pip3 install PyYAML
#  fi
#pip3 install pymongo
#DIRPATH=/home/"$(echo "$(echo "$(w -h -s)" | cut -c1-9)" | xargs)"/LogsCol
#SIZEDIR="$(du -sh "$DIRPATH/rejected_pkt" | cut -c1-5)"
#df=$(echo "${SIZEDIR//[[:blank:]]/}")
#if [ -d  "$DIRPATH" ] && [ "$(du -sh $DIRPATH | cut -c1-5)" -ge 50 ];then echo "";fi
python3 -c "$PYCMD "
#python3 --version