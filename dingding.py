#!/usr/bin/python
#author:wolfsun
# -*- coding: utf-8 -*-
import requests
import json
import sys
#import os
 
headers = {'Content-Type': 'application/json;charset=utf-8'}
api_url = "dingding webhook url"

def msg(text):
    json_text= {
     "msgtype": "text",
        "text": {
            "content": text
        }
#可以加上相应的at 属性，对应个别重要的人或者所有人；
#        "at": {
#            "atMobiles": [
#                "18710019783"
#            ],
#            "isAtAll": True
#        }
    }
    requests.post(api_url,json.dumps(json_text),headers=headers).content
     
if __name__ == '__main__':
    text = sys.argv[1]
    msg(text)
