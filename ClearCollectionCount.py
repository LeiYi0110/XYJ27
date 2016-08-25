# -*- coding: utf-8 -*-
__author__ = 'wanglei'


import mysql.connector
import json
import pymongo
con = pymongo.MongoClient("120.25.207.34", 27017)

db = con.xyj
db.authenticate("xyj", "xyj88283088")
db.common_data.update_many(
    {"collection_count": {"$lt": 0}},
    {
        "$set":{"collection_count":0}

    }
)

db.hotel.update_many(
    {"collection_count": {"$lt": 0}},
    {
        "$set":{"collection_count":0}

    }
)

db.restaurant.update_many(
    {"collection_count": {"$lt": 0}},
    {
        "$set":{"collection_count":0}

    }
)
db.sights.update_many(
    {"collection_count": {"$lt": 0}},
    {
        "$set":{"collection_count":0}

    }
)
