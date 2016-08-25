# -*- coding: utf8 -*-
__author__ = 'wanglei'


import pymongo
import mysql.connector
from bson.objectid import ObjectId

from datetime import *



from threading import Timer


con = pymongo.MongoClient("120.25.207.34", 27017)

db = con.xyj
db.authenticate("xyj", "xyj88283088")

mysql_user = 'tour'
mysql_pwd = 'Tour@2015'
mysql_host = '120.25.207.34'
mysql_connect_database = 'tour'

cnxXYJ = mysql.connector.connect(user='tour', password='Tour@2015', host='120.25.207.34', database='xyj_common_dev')


cursorXYJ = cnxXYJ.cursor()


host = "http://www.xiangyouji.com.cn:3000/"
theme_id = 1
cursorXYJ.execute('select * from tour_route where id = 60')
route_list = []
for route_item in cursorXYJ:
    route_list.append(route_item)
    print route_item

route_result_list = []
for route_item in route_list:
    image_list = []
    cursorXYJ.execute('select * from entity_image where entity_id = ' + str(route_item[0]))
    for image_item in cursorXYJ:
        image_list.append({"url": host + image_item[4],"update_time":datetime.now(),"create_time":datetime.now(),"order":image_item[1]})

    db.tour_route.update_one({"_id":ObjectId("567fe57d9cbda0120d6f5c2d")},{"$set":{"shop_id": "", "route_name": route_item[1], "route_address": route_item[2], "route_desc": route_item[4],
                     "route_telephone": route_item[3], "city_id": 235, "area_id": -1, "province": 21,
                     "gps": {"longitude": route_item[6], "latitude": route_item[5]}, "create_time": datetime.now(),
                     "update_time": datetime.now(),  "cover": host + route_item[7], "images": image_list, "collection_count": 0,"desc_file":host + route_item[9],"theme_id":theme_id,"price":99}})

    '''
    db.tour_route.insert({"shop_id": "", "route_name": route_item[1], "route_address": route_item[2], "route_desc": route_item[4],
                     "route_telephone": route_item[3], "city_id": 235, "area_id": -1, "province": 21,
                     "gps": {"longitude": route_item[6], "latitude": route_item[5]}, "create_time": datetime.now(),
                     "update_time": datetime.now(),  "cover": host + route_item[7], "images": image_list, "collection_count": 0,"desc_file":host + route_item[9],"theme_id":theme_id,"price":99})
    '''

'''
cursorXYJ.execute('select * from theme where id = ' + str(theme_id))

for themeItem in cursorXYJ:
    print themeItem
    curor = db['tour_route'].find({"theme_id":theme_id})
    entity_list = []
    i = 0
    for route_item in curor:
        entity_list.append({"area_id":route_item["area_id"],"name":route_item["route_name"],"collected_count":route_item["collection_count"],"entity_type":4,"entity_id":route_item["_id"],"images":route_item["images"],"order":i,"url":route_item["cover"],"gps":route_item["gps"],"comment_count":0})
        i = i + 1
    db.theme.insert({"province":21,"title":themeItem[1],"cover":host + themeItem[4],"order":0,"gps": {"longitude": 109.73375548794, "latitude": 19.180500801261},"entities":entity_list,"update_time":datetime.now()})
        #print route_item



'''












'''
db.hotel.insert({"shop_id": "", "hotel_name": entity.name, "hotel_address": entity.address, "hotel_desc": entity.desc,
                     "hotel_telephone": entity.phone, "city_id": entity.city, "area_id": entity.area_id, "province": entity.province,
                     "gps": {"longitude": entity.gps.longitude, "latitude": entity.gps.latitude}, "create_time": datetime.now(),
                     "update_time": datetime.now(), "lowest_price": 0.0, "room_value": 0.0, "location_value": 0.0,
                     "service_value": 0.0, "avg_price": 0.0, "star_count": 0.0, "cover": cover, "images": entity.imageList, "city":entity.city, "collection_count": 0, "comment_count": 0})
'''

'''
def updateEntity():
    curor = db['theme'].find()
    themes = []
    for item in curor:
        themes.append(item)

    for item in themes:
        entity_list = []
        old_entity_list = item["entities"]
        for entityItem in old_entity_list:
            real_entity = db.common_data.find_one({"entity_type":entityItem["entity_type"],"entity_id":ObjectId(entityItem["entity_id"])})
            print real_entity
            entityItem["collected_count"] = real_entity["collection_count"]
            entityItem["comment_count"] = real_entity["comment_count"]
            #entityItem["area_id"] = real_entity["area_id"]
            entity_list.append(entityItem)
        db.theme.update_one({"_id":ObjectId(item["_id"])},{"$set":{"entities":entity_list,"update_time":datetime.now()}})

    t = Timer(5*60,updateEntity)
    t.start()
updateEntity()
'''

