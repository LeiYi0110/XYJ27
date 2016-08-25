# -*- coding: utf8 -*-
__author__ = 'wanglei'


import sys,os,json,httplib
import mysql.connector
import pymongo

from datetime import *


print "hello new debian"

class Location:
    def __init__(self):
        self.latitude = 0.0
        self.longitude = 0.0

def get_location(address):

    #print address
    conn = httplib.HTTPConnection("api.map.baidu.com")
    #conn.request("GET","/geocoder/v2/?address=青岛市市南区观象二路21号（观象山公园中心）&output=json&ak=aez4EuqcDUoOF7oKwPFsyijv&callback=showLocation")
    url = "/geocoder/v2/?address=" + address.encode('utf8') + "&output=json&ak=aez4EuqcDUoOF7oKwPFsyijv&callback=showLocation"
    conn.request("GET",url)
    r1 = conn.getresponse()
    #print(r1.status, r1.reason)
    data1 = r1.read()
    #print data1
    start = data1.find('({')
    end = data1.find('})')

    location = Location()
    try:
        jsonData = json.loads(data1[start + 1:end + 1])
        location.latitude = jsonData["result"]["location"]["lat"]
        location.longitude = jsonData["result"]["location"]["lng"]
    except:
        pass




    return location


con = pymongo.MongoClient("120.25.207.34", 27017)
db = con.xyj
db.authenticate("xyj", "xyj88283088")
#print db.test.find_one({})

hotelList = []


cnxXYJ = mysql.connector.connect(user='tour', password='Tour@2015', host='120.25.207.34', database='xyj_common_dev')


cursorXYJ = cnxXYJ.cursor()

cursorXYJ.execute('select * from area_province')
provinceList = []
#cityList = []
#areaList = []

southList = []
eastList = []
northList = []
northWestList = []
southWestList = []
northEastList = []

otherList = []


result = []
i = 0


class Location:
    def __init__(self):
        self.latitude = 0.0
        self.longitude = 0.0


def exists_in_entity(area_id):
    cursor_entity = db.common_data.find({"area_id":area_id})
    #print "len :", len(cursor_entity)
    entity_list = []
    for entityItem in cursor_entity:
        entity_list.append(cursor_entity)
    print len(entity_list)
    if len(entity_list) > 0:
        return True
    return False


def get_location(address):

    print address
    conn = httplib.HTTPConnection("api.map.baidu.com")
    url = "/geocoder/v2/?address=" + address.encode('utf8') + "&output=json&ak=aez4EuqcDUoOF7oKwPFsyijv&callback=showLocation"
    conn.request("GET",url)
    r1 = conn.getresponse()
    print(r1.status, r1.reason)
    data1 = r1.read()
    print data1
    start = data1.find('({')
    end = data1.find('})')

    location = Location()
    try:
        jsonData = json.loads(data1[start + 1:end + 1])
        location.latitude = jsonData["result"]["location"]["lat"]
        location.longitude = jsonData["result"]["location"]["lng"]
    except:
        pass

    return location


for provinceItem in cursorXYJ:
    provinceList.append(provinceItem)

for provinceItem in provinceList:
    if provinceItem[0] >= 19 and provinceItem[0] <= 21:
        southList.append(provinceItem)
print southList

for provinceItem in provinceList:
    if provinceItem[0] >= 9 and provinceItem[0] <= 14:
        eastList.append(provinceItem)
print eastList

for provinceItem in provinceList:
    if provinceItem[0] >= 1 and provinceItem[0] <= 5:
        northList.append(provinceItem)
print northList

for provinceItem in provinceList:
    if provinceItem[0] >= 22 and provinceItem[0] <= 26:
        southWestList.append(provinceItem)
print southWestList

'''
un_show_city_list = []
cursorXYJ.execute("SELECT * FROM tour.area_city where province_id in (1,2,9,22) union select * from tour.area_city where name like '省%'")
for un_show_item in cursorXYJ:
    un_show_city_list.append(un_show_item)
    print un_show_item
'''

for provinceItem in provinceList:
    print provinceItem
    cursorXYJ.execute('select * from area_city where province_id = ' + str(provinceItem[0]))
    cityList = []
    for cityItem in cursorXYJ:
        cityList.append(cityItem)
    #db.area.insert({"provinceId": provinceItem[0], "provinceName": provinceItem[1]})
    cityResult = []

    for cityItem in cityList:
        areaList = []

        cursorXYJ.execute('select * from area_county where city_id = ' + str(cityItem[0]))
        for areaItem in cursorXYJ:
            if exists_in_entity(areaItem[0]):
                gps = get_location(provinceItem[1] + cityItem[1] + areaItem[1])
                areaList.append({"area_id":areaItem[0], "area_name":areaItem[1].strip(), "gps": {"latitude":gps.latitude, "longitude":gps.longitude}})
                db.current_area_data.insert({"area_id":areaItem[0], "area_name":areaItem[1].strip(), "gps": {"latitude":gps.latitude, "longitude":gps.longitude}})


        #db.area.insert({"provinceId": provinceItem[0], "provinceName": provinceItem[1]})

        if len(areaList) > 0:
            city_id = cityItem[0]
            is_show = 1
            if city_id == 1 or city_id == 3 or city_id == 75 or city_id == 238 or city_id == 185 or city_id == 237 or city_id == 344:
                is_show = 0

            #cityResult.append({"cityId":cityItem[0], "cityName": cityItem[1], "area":areaList})
            cityResult.append({"cityId":city_id, "cityName": cityItem[1].strip(), "isShow": is_show, "area":areaList})
    region = ""
    if provinceItem[0] >= 19 and provinceItem[0] <= 21:
        region = "south"
    elif provinceItem[0] >= 9 and provinceItem[0] <= 14:
        region = "east"
    elif provinceItem[0] >= 1 and provinceItem[0] <= 5:
        region = "north"
    elif provinceItem[0] >= 22 and provinceItem[0] <= 26:
        region = "southwest"
    else:
        region = "other"

    if len(cityResult) > 0:
        provinceName = provinceItem[1].strip()[0:2]
        if provinceName == "黑龙" or provinceName == "内蒙":
            provinceName = provinceItem[1].strip()[0:3]
        location = get_location(provinceName)
        db.current_area.insert({"provinceId": provinceItem[0], "provinceName": provinceName, "region":region, "city": cityResult,"gps":{"latitude":location.latitude,"longitude":location.longitude}})

    print cityResult





cnxXYJ.close()



'''
curor = db['hotel'].find({"province":provinceItem[0]}).skip(0).limit(7)
    hotelList = []
    for entityItem in curor:
        hotelList.append(entityItem)
'''