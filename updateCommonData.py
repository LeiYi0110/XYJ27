# -*- coding: utf8 -*-
__author__ = 'wanglei'


import pymongo
from bson.objectid import ObjectId

from datetime import *



from threading import Timer


con = pymongo.MongoClient("120.25.207.34", 27017)

db = con.xyj
db.authenticate("xyj", "xyj88283088")





def updateEntity():
    curor = db['common_data'].find()
    common_data_list = []
    for item in curor:
        common_data_list.append(item)

    for item in common_data_list:

        entity_type = item["entity_type"]
        entity_id = item["entity_id"]

        entity_collection = ""
        if entity_type == 1:
            entity_collection = "hotel"
        elif entity_type == 2:
            entity_collection = "restaurant"
        elif entity_type == 3:
            entity_collection = "sights"

        real_entity = db[entity_collection].find_one({"_id":ObjectId(entity_id)})
        print entity_collection
        print real_entity
        #print real_entity["collection_count"], real_entity["comment_count"]
        db.common_data.update_one({"_id":ObjectId(item["_id"])},{"$set":{"collection_count":real_entity["collection_count"],"comment_count":real_entity["comment_count"]}})
        '''
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
        '''

updateEntity()


