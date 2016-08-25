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


theme = db['theme'].find_one({"_id":ObjectId("567fe57d9cbda0120d6f5c2e")})
print theme
old_entity_list = theme["entities"]
entity_list = []

#db.theme.update_one({"_id":ObjectId(theme["_id"])},{"$set":{"entities":entity_list}})

for entity_item in old_entity_list:
    entity_list.append(entity_item)

i = len(entity_list)


print theme["_id"]


host = "http://www.xiangyouji.com.cn:3000/"
theme_id = 1
cursorXYJ.execute('select * from tour_route where is_import = 0')
route_list = []
for route_item in cursorXYJ:
    route_list.append(route_item)
    print route_item


for route_item in route_list:
    image_list = []
    cursorXYJ.execute('select * from entity_image where entity_id = ' + str(route_item[0]))
    for image_item in cursorXYJ:
        image_list.append({"url": host + image_item[4],"update_time":datetime.now(),"create_time":datetime.now(),"order":image_item[1]})


    #route_result_item =
    #route_result_list.append(route_result_item)
    db.tour_route.insert({"shop_id": "", "route_name": route_item[1], "route_address": route_item[2], "route_desc": route_item[4],
                     "route_telephone": route_item[3], "city_id": 235, "area_id": -1, "province": 21,
                     "gps": {"longitude": route_item[6], "latitude": route_item[5]}, "create_time": datetime.now(),
                     "update_time": datetime.now(),  "cover": host + route_item[7], "images": image_list,
                     "collection_count": 0,"desc_file":host + route_item[9],"theme_id":theme_id,"price":route_item[10],
                     "raw_id":route_item[0]})

    #cursorXYJ.execute('update tour_route set is_import = 1 where id = ' + str(route_item[0]))
    entity = db.tour_route.find_one({"raw_id":route_item[0]})

    entity_list.append({"area_id":entity["area_id"],"name":entity["route_name"],"collected_count":entity["collection_count"],"entity_type":4,"entity_id":entity["_id"],"images":entity["images"],"order":i,"url":entity["cover"],"gps":entity["gps"],"comment_count":0})
    #entity_list.append(entity)
    i = i + 1

db.theme.update_one({"_id":ObjectId(theme["_id"])},{"$set":{"entities":entity_list}})










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
curor = db['tour_route'].find({"theme_id":1})
entity_list = []
i = 0
for route_item in curor:
    entity_list.append({"area_id":route_item["area_id"],"name":route_item["route_name"],"collected_count":route_item["collection_count"],"entity_type":4,"entity_id":route_item["_id"],"images":route_item["images"],"order":i,"url":route_item["cover"],"gps":route_item["gps"],"comment_count":0})
    i = i + 1
db.theme.update_one({"_id":ObjectId(theme["_id"])},{"$set":{"entities":entity_list}})
'''

