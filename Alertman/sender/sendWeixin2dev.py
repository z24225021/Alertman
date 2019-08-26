#!/bin/python
#-*- coding: utf-8 -*-

import requests
import sys
import os
import json
import logging
import time

from settings import ALERT_USER

try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

logging.basicConfig(level = logging.INFO, format = '%(asctime)s, %(filename)s, %(levelname)s, %(message)s',
                datefmt = '%a, %d %b %Y %H:%M:%S',
                filename = os.path.join('/tmp','weixin.log'),
                filemode = 'a')
def sendweixin2dev(subject,message,user):
    print "告警内容:",(subject,message)
    msgsend_url = 'https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    params = {
    "title": subject,
    "message": message,
    "users": user,
    "apiKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
    header = {'content-type': 'application/json'}
    req=requests.post(msgsend_url, data=json.dumps(params,ensure_ascii=False),headers=header)
    print req
    # 写日志
    #logging.info('sendto:' + touser + ';;subject:' + subject + ';;message:' + message)
if __name__=="__main__":
    sendweixin2dev(sys.argv[1],sys.argv[2],sys.argv[3])
