# -*- coding: utf8 -*-
__author__ = 'wanglei'

import sys,os,json,httplib

import mysql.connector

import pymongo
from bson.objectid import ObjectId

import types

from datetime import *

import uuid

import urllib

con = pymongo.MongoClient("120.25.207.34", 27017)

db = con.xyj
db.authenticate("xyj", "xyj88283088")

entity = 'sights'

curor = db[entity].find()
entity_list = []
for item in curor:
    entity_list.append(item)
for entityItem in entity_list:
    print entityItem
    db[entity].update_one({"_id":ObjectId(entityItem["_id"])},{"$set":{"avg_price_count": 0}})