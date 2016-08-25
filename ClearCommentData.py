# -*- coding: utf-8 -*-
__author__ = 'wanglei'


import mysql.connector
import json
import pymongo
from bson.objectid import ObjectId
con = pymongo.MongoClient("120.25.207.34", 27017)

db = con.xyj
db.authenticate("xyj", "xyj88283088")

'''
curor = db['hotel'].find()
entity_list = []

for item in curor:
    entity_list.append(item)

for item in entity_list:
    print item
    db.hotel.update_one({"_id":ObjectId(item["_id"])},{"$set":{"service_value":0,"location_value":0,"room_value":0,"star_count":0,"comment_count":0,"avg_price":0,"avg_price_count":0}})



curor = db['restaurant'].find()
entity_list = []

for item in curor:
    entity_list.append(item)

for item in entity_list:
    print item
    db.restaurant.update_one({"_id":ObjectId(item["_id"])},{"$set":{"service_value":0,"taste_value":0,"environment_value":0,"star_count":0,"comment_count":0,"avg_price":0,"avg_price_count":0}})

'''
curor = db['sights_comment'].find()
entity_list = []

for item in curor:
    entity_list.append(item)

for item in entity_list:
    print item
    db.sights.update_one({"_id":ObjectId(item["sights_id"])},{"$set":{"star_count":0,"comment_count":0,"avg_price":0,"avg_price_count":0}})