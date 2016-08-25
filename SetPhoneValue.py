__author__ = 'wanglei'


import pymongo
from bson.objectid import ObjectId
from datetime import *


print "hello new debian"

con = pymongo.MongoClient("120.25.207.34", 27017)

db = con.xyj
db.authenticate("xyj", "xyj88283088")

curor = db['hotel'].find()

#hotel_list = []

for item in curor:
    print item
    '''
    db['hotel_test'].insert({"area_id": item["area_id"], "name": item["hotel_name"], "address": item["hotel_address"],
                              "phone": item["hotel_telephone"], "gps": item["gps"], "cover": item["cover"],
                              "entity_id": item["_id"], "entity_type": 1, "province": item["province"], "images": item["images"], "collection_count": 0, "comment_count": 0})
    '''

    p_value = item["hotel_telephone"]
    if(len(p_value)) > 0:
        phone_value = str(long((float(p_value))))
        print phone_value
        db.hotel.update_one({"_id":ObjectId(item["_id"])},{"$set":{"hotel_telephone":phone_value}})





curor = db['restaurant'].find()

for item in curor:
    print item
    '''
    db['restaurant_test'].insert({"area_id": item["area_id"], "name": item["restaurant_name"],
                              "address": item["restaurant_address"],
                              "phone": item["restaurant_telephone"], "gps": item["gps"], "cover": item["cover"],
                              "entity_id": item["_id"], "entity_type": 2, "province": item["province"], "images": item["images"], "collection_count": 0, "comment_count": 0})
    '''
    p_value = item["restaurant_telephone"]
    if(len(p_value)) > 0:
        phone_value = str(long((float(p_value))))
        print phone_value
        db.restaurant.update_one({"_id":ObjectId(item["_id"])},{"$set":{"restaurant_telephone":phone_value}})

curor = db['sights'].find()

for item in curor:
    print item
    '''
    db['common_data'].insert({"area_id": item["area_id"], "name": item["sights_name"],
                              "address": item["sights_address"],
                              "phone": item["sights_telephone"], "gps": item["gps"], "cover": item["cover"],
                              "entity_id": item["_id"], "entity_type": 3, "province": item["province"], "images": item["images"],"collection_count": 0, "comment_count": 0})
    '''
    p_value = item["sights_telephone"]
    if(len(p_value)) > 0:
        phone_value = str(long((float(p_value))))
        print phone_value
        db.sights.update_one({"_id":ObjectId(item["_id"])},{"$set":{"sights_telephone":phone_value}})





