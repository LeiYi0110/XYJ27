# -*- coding: utf8 -*-
__author__ = 'wanglei'

import sys,os,json,httplib

import mysql.connector

import pymongo

import types

from datetime import *

import uuid

import urllib

con = pymongo.MongoClient("120.25.207.34", 27017)

db = con.xyj
db.authenticate("xyj", "xyj88283088")

mysql_user = 'tour'
mysql_pwd = 'Tour@2015'
mysql_host = '120.25.207.34'
mysql_connect_database = 'tour'

def get_province_name(province_id):
    province_name = ""
    cnxXYJ = mysql.connector.connect(user=mysql_user, password=mysql_pwd, host=mysql_host, database=mysql_connect_database)

    cursorXYJ = cnxXYJ.cursor()
    cursorXYJ.execute("select name from area_province where id = " + str(province_id))
    for item in cursorXYJ:
        province_name = item[0]
    cnxXYJ.close()
    return province_name


curor = db['area'].find()
province_list = []

for item in curor:
    #print item["provinceName"]
    province_list.append(item)

for item in province_list:
    province_name = item["provinceName"]
    while len(province_name) < 7:
        province_name = province_name + '  '
    print province_name  + '  ' + str(db.sights.count({"province":item["provinceId"]})) + '  ' + str(db.restaurant.count({"province":item["provinceId"]})) + '  ' + str(db.hotel.count({"province":item["provinceId"]}))

#print db.hotel.count({"province":25})
