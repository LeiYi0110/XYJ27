# -*- coding: utf-8 -*-
__author__ = 'wanglei'


import mysql.connector
import json
import pymongo

from datetime import *


print "hello new debian"

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

con = pymongo.MongoClient("120.25.207.34", 27017)

db = con.xyj
db.authenticate("xyj", "xyj88283088")



for provinceItem in cursorXYJ:
    provinceList.append(provinceItem)


for provinceItem in provinceList:
    themeList = []
    curor = db['hotel'].find({"province":provinceItem[0]})
    hotelList = []
    i = 0
    for entityItem in curor:
        if len(entityItem['cover']) > 0:
            hotelList.append(entityItem)
            i = i + 1
            if i == 7:
                break

    if len(hotelList) == 0:
        continue
    #print entityList[0]

    cover = hotelList[0]['cover']
    hotels = []
    for i in range(1, len(hotelList)):
        hotels.append({"url":hotelList[i]["cover"], "order":i, "entity_type":1, "entity_id":hotelList[i]["_id"], "images":hotelList[i]["images"], "gps":hotelList[i]["gps"], "collected_count":0,"name":hotelList[i]["hotel_name"]})
    title = unicode(u"住山庄主题")
    #db.theme.insert({"province":provinceItem[0],"cover":cover, "title":title, "entities":entities, "order": 1})
    themeList.append({"cover":cover, "title":title, "entities":hotels, "order": 1})
    db.theme2.insert({"cover":cover, "title":title, "entities":hotels, "order": 1, "province":provinceItem[0]})


    curor = db['restaurant'].find({"province":provinceItem[0]}).skip(0).limit(7)
    restaurantList = []
    i = 0
    for entityItem in curor:
        if len(entityItem['cover']) > 0:
            restaurantList.append(entityItem)
            i = i + 1
            if i == 7:
                break
    if len(restaurantList) == 0:
        continue
    #print entityList[0]

    cover = restaurantList[0]['cover']
    restaurants = []
    for i in range(1, len(restaurantList)):
        restaurants.append({"url":restaurantList[i]["cover"], "order":i, "entity_type":2, "entity_id":restaurantList[i]["_id"], "images": restaurantList[i]["images"], "gps":restaurantList[i]["gps"], "collected_count":0,"name":restaurantList[i]["restaurant_name"]})
    title = unicode(u"吃乡味主题")
    themeList.append({"cover":cover, "title":title, "entities":restaurants, "order": 2})
    db.theme2.insert({"cover":cover, "title":title, "entities":restaurants, "order": 2, "province":provinceItem[0]})



    curor = db['sights'].find({"province":provinceItem[0]}).skip(0).limit(7)
    sightsList = []
    i = 0
    for entityItem in curor:
        if len(entityItem['cover']) > 0:
            sightsList.append(entityItem)
            i = i + 1
            if i == 7:
                break
    if len(sightsList) == 0:
        continue
    #print entityList[0]

    cover = sightsList[0]['cover']
    sights = []
    for i in range(1, len(sightsList)):
        sights.append({"url":sightsList[i]["cover"], "order":i, "entity_type":3, "entity_id":sightsList[i]["_id"], "images": sightsList[i]["images"], "gps":sightsList[i]["gps"], "collected_count":0,"name":sightsList[i]["sights_name"]})
    title = unicode(u"游美景主题")
    themeList.append({"cover":cover, "title":title, "entities":sights, "order": 3})
    db.theme2.insert({"cover":cover, "title":title, "entities":sights, "order": 3, "province":provinceItem[0]})

    #db.theme.insert({"province":provinceItem[0],"themes":themeList})




#db.theme.insert("provice":1,cover:"",images:[{"url":1,"order":""], "order":)


'''

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
            areaList.append({"area_id":areaItem[0], "area_name":areaItem[1]})
        #db.area.insert({"provinceId": provinceItem[0], "provinceName": provinceItem[1]})
        cityResult.append({"cityId":cityItem[0], "cityName": cityItem[1], "area":areaList})
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


    db.area.insert({"provinceId": provinceItem[0], "provinceName": provinceItem[1], "region":region, "city": cityResult})
    print cityResult

'''

cnxXYJ.close()




