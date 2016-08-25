# -*- coding: utf-8 -*-
__author__ = 'wanglei'


import hashlib

src = '123'
m2 = hashlib.md5()
m2.update(src)
print m2.hexdigest()
print len(m2.hexdigest())
print m2.digest_size


import md5
src = 'SDK-LJP-010-00110031268'
m1 = md5.new()
m1.update(src)
print m1.hexdigest().upper()


import os
import httplib
import json
import urllib
content = "你好乡游记"


params = urllib.urlencode({'sn': 'SDK-LJP-010-00110', 'pwd': '51FC662DD2521E748D699B8D160BCCD5', 'mobile': '13686840267','content': "或许我们最近又有误会了【乡游记】",'ext':'', 'stime':'', 'rrid':'', 'msgfmt':'15'})
conn = httplib.HTTPConnection("sdk.entinfo.cn",8061)

headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "Content-Length": len(params)}

conn.request("POST","/webservice.asmx/mdsmssend",params,headers)

#conn.request("GET", "/webservice.asmx/gxmt?sn=SDK-LJP-010-00110&pwd=51FC662DD2521E748D699B8D160BCCD5&mobile=18680668215&content=aabbccd&ext=&stime=&rrid=")
r1 = conn.getresponse()
print(r1.status,r1.reason)
data1 = r1.read()
print data1




