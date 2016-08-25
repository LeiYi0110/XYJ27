# -*- coding: utf8 -*-
__author__ = 'wanglei'


import pymongo
from bson.objectid import ObjectId
import geojson
from geojson import Point
from datetime import *


print "hello new debian"

con = pymongo.MongoClient("120.25.207.34", 27017)

db = con.xyj
db.authenticate("xyj", "xyj88283088")
'''
curor = db['hotel'].find()

list = []

for item in curor:
    list.append(item)

for item in list:
    print item

    latitude = item["gps"]["latitude"]
    longitude = item["gps"]["longitude"]
    print latitude,longitude
    gps_point = Point((longitude,latitude))
    print gps_point
    db.hotel.update_one({"_id":ObjectId(item["_id"])},{"$set":{"gps_sphere_3": gps_point}})





restaurant_list = []



curor = db['restaurant'].find()

for item in curor:
    restaurant_list.append(item)

for item in restaurant_list:
    print item

    latitude = item["gps"]["latitude"]
    longitude = item["gps"]["longitude"]
    print latitude,longitude
    gps_point = Point((longitude,latitude))
    print gps_point
    db.restaurant.update_one({"_id":ObjectId(item["_id"])},{"$set":{"gps_sphere_3": gps_point}})

'''
curor = db['sights'].find()
sights_list = []

for item in curor:
    sights_list.append(item)

for item in sights_list:
    print item
    #'%.2f'%103.4
    latitude = item["gps"]["latitude"]
    longitude = item["gps"]["longitude"]
    print latitude,longitude
    gps_point = Point((longitude,latitude))
    print gps_point
    db.sights.update_one({"_id":ObjectId(item["_id"])},{"$set":{"gps_sphere_3": gps_point}})







