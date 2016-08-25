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


