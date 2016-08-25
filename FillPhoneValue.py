__author__ = 'wanglei'


import pymongo
from bson.objectid import ObjectId
import random
from datetime import *


print "hello new debian"

con = pymongo.MongoClient("120.25.207.34", 27017)

db = con.xyj
db.authenticate("xyj", "xyj88283088")

#phone_value = str(long((float("18005937692.0"))))
#print phone_value



curor = db['restaurant'].find()
entity_list = []
for item in curor:
    print item
    entity_list.append(item)
for item in entity_list:
    db.restaurant.update_one({"_id":ObjectId(item["_id"])},{"$set":{"is_preferential":1}})
'''
for item in entity_list:
    try:
        #phone_value = db.phoneData2.find_one({"entity_name":item["sights_name"]})["phone"]
        #print phone_value.strip()
        db.common_data.update_one({"_id":ObjectId(item["_id"])},{"$set":{"collection_count":0}})
    except:
        pass
'''

#round(random.uniform(8, 9),1)

#discount
'''
curor = db['phoneData'].find()

phone_data_list = []

for item in curor:
    phone_data_list.append(item)

for item in phone_data_list:
    try:
        phone_value = str(long((float(item["phone"]))))
        db.phoneData2.insert({"entity_name":item["entity_name"],"phone":phone_value})
        print phone_value
    except:
        db.phoneData2.insert({"entity_name":item["entity_name"],"phone":item["phone"]})
        pass
'''
