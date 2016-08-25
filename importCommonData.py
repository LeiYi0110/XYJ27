__author__ = 'wanglei'

import pymongo

from datetime import *


print "hello new debian"

con = pymongo.MongoClient("120.25.207.34", 27017)

db = con.xyj
db.authenticate("xyj", "xyj88283088")

curor = db['hotel'].find()

for item in curor:
    print item
    db['common_data'].insert({"area_id": item["area_id"], "name": item["hotel_name"], "address": item["hotel_address"],
                              "phone": item["hotel_telephone"], "gps": item["gps"], "cover": item["cover"],
                              "entity_id": item["_id"], "entity_type": 1, "province": item["province"], "images": item["images"], "collection_count": 0, "comment_count": 0})

curor = db['restaurant'].find()

for item in curor:
    print item
    db['common_data'].insert({"area_id": item["area_id"], "name": item["restaurant_name"],
                              "address": item["restaurant_address"],
                              "phone": item["restaurant_telephone"], "gps": item["gps"], "cover": item["cover"],
                              "entity_id": item["_id"], "entity_type": 2, "province": item["province"], "images": item["images"], "collection_count": 0, "comment_count": 0})

curor = db['sights'].find()

for item in curor:
    print item
    db['common_data'].insert({"area_id": item["area_id"], "name": item["sights_name"],
                              "address": item["sights_address"],
                              "phone": item["sights_telephone"], "gps": item["gps"], "cover": item["cover"],
                              "entity_id": item["_id"], "entity_type": 3, "province": item["province"], "images": item["images"],"collection_count": 0, "comment_count": 0})




