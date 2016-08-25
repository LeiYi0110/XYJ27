# -*- coding: utf-8 -*-
__author__ = 'wanglei'


import os
import httplib
import json

conn = httplib.HTTPConnection("api.map.baidu.com")

#conn.request("GET","/geocoder/v2/?address=百度大厦&output=json&ak=aez4EuqcDUoOF7oKwPFsyijv&callback=showLocation")
conn.request("GET","/geocoder/v2/?address=河北承德隆化&output=json&ak=aez4EuqcDUoOF7oKwPFsyijv&callback=showLocation")
r1 = conn.getresponse()
print(r1.status, r1.reason)
data1 = r1.read()
print data1

start = data1.find('({')
end = data1.find('})')
print start
print end

#jsonData = json.loads(data1[start:end])
print(data1[start + 1:end + 1])

jsonData = json.loads(data1[start + 1:end + 1])
print jsonData
print jsonData["result"]["location"]

for key in jsonData.keys():
    print jsonData[key]




#showLocation&&showLocation({"status":0,"result":{"location":{"lng":114.17582579975,"lat":22.574291920606},"precise":1,"confidence":80,"level":"\u9053\u8def"}})

#:{"location":{"lng":113.18665531066,"lat":23.195011165357},
