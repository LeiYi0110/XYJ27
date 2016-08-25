# -*- coding: utf8 -*-
__author__ = 'wanglei'


import pymongo
from bson.objectid import ObjectId
import geojson
from geojson import Point
from datetime import *
import httplib,json,urllib
import mysql.connector


con = pymongo.MongoClient("120.25.207.34", 27017)

db = con.xyj
db.authenticate("xyj", "xyj88283088")


def get_entity_by_name(entity_name):
    entity = Entity()
    try:
        result_entity = db.common_data.find_one({"name":entity_name})
        entity.address = result_entity["address"]
        entity.entity_type = result_entity["entity_type"]
        entity.name = result_entity["name"]
        entity.imageList = result_entity["images"]
        entity.phone = result_entity["phone"]
        entity.gps = result_entity["gps"]
        entity.province = result_entity["province"]
        entity.area_id = result_entity["area_id"]
        entity.entity_id = result_entity["entity_id"]

        return entity
    except:
        pass
    return None

curor = db['theme'].find()
themes = []
for item in curor:
    themes.append(item)
'''
for item in themes:
    db.theme.update_one({"_id":ObjectId(item["_id"])},{"$unset":{"collected_count":0}})
'''
'''
for item in themes:
    entity_list = []
    old_entity_list = item["entities"]
    for entityItem in old_entity_list:
        if entityItem["gps"]["latitude"] == 0:
            theEntity = db.common_data.find_one({"entity_id":ObjectId(entityItem["entity_id"])})
            if theEntity["gps"]["latitude"] != 0:
                entity_list.append(theEntity)
                #print theEntity["entity_id"], theEntity["gps"]
        else:
            entity_list.append(entityItem)

    db.theme.update_one({"_id":ObjectId(item["_id"])},{"$set":{"entities":entity_list}})

'''

'''
for item in themes:
    entity_list = []
    old_entity_list = item["entities"]
    for entityItem in old_entity_list:
        entityItem["collected_count"] = 0
        entity_list.append(entityItem)


    db.theme.update_one({"_id":ObjectId(item["_id"])},{"$set":{"entities":entity_list}})
'''


'''
for item in themes:
    entity_list = []
    old_entity_list = item["entities"]
    for entityItem in old_entity_list:

        try:
            order = (entityItem["order"])

        except:
            entityItem["order"] = -1
            pass

        entity_list.append(entityItem)

    db.theme.update_one({"_id":ObjectId(item["_id"])},{"$set":{"entities":entity_list}})
'''
for item in themes:
    entity_list = []
    old_entity_list = item["entities"]
    for entityItem in old_entity_list:
        try:
            real_entity = db.common_data.find_one({"entity_type":entityItem["entity_type"],"entity_id":ObjectId(entityItem["entity_id"])})
            print real_entity
            #print entityItem["collected_count"]
        except:
            print entityItem
            pass


