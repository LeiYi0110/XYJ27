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

mysql_user = 'tour'
mysql_pwd = 'Tour@2015'
mysql_host = '120.25.207.34'
mysql_connect_database = 'tour'

#con = pymongo.MongoClient("120.25.207.34", 27017)


class Location:
    def __init__(self):
        self.latitude = 0.0
        self.longitude = 0.0

def get_province_name(province_id):
    province_name = ""
    cnxXYJ = mysql.connector.connect(user=mysql_user, password=mysql_pwd, host=mysql_host, database=mysql_connect_database)

    cursorXYJ = cnxXYJ.cursor()
    cursorXYJ.execute("select name from area_province where id = " + str(province_id))
    for item in cursorXYJ:
        province_name = item[0]
    cnxXYJ.close()
    return province_name

def get_city_name(city_id):
    city_name = ""
    cnxXYJ = mysql.connector.connect(user=mysql_user, password=mysql_pwd, host=mysql_host, database=mysql_connect_database)

    cursorXYJ = cnxXYJ.cursor()
    cursorXYJ.execute("select name from area_city where id = " + str(city_id))
    for item in cursorXYJ:
        city_name = item[0]
    cnxXYJ.close()
    return city_name

def get_area_name(area_id):
    area_name = ""
    cnxXYJ = mysql.connector.connect(user=mysql_user, password=mysql_pwd, host=mysql_host, database=mysql_connect_database)

    cursorXYJ = cnxXYJ.cursor()
    cursorXYJ.execute("select name from area_county where id = " + str(area_id))
    for item in cursorXYJ:
        area_name = item[0]
    cnxXYJ.close()
    return area_name


def get_location(address):

    #print address
    conn = httplib.HTTPConnection("api.map.baidu.com")

    url = "/geocoder/v2/?address=" + address.encode('utf8') + "&output=json&ak=aez4EuqcDUoOF7oKwPFsyijv&callback=showLocation"
    '''
    url_arr = url.split(" ")

    result = ""
    for urlItem in url_arr:
        result += urlItem
    '''
    url = url.replace(" ","")





    print url
    conn.request("GET",url)
    r1 = conn.getresponse()
    #print(r1.status, r1.reason)
    data1 = r1.read()
    #print data1
    start = data1.find('({')
    end = data1.find('})')
    #print json.loads(data1[start + 1:end + 1])
    location = Location()
    try:
        jsonData = json.loads(data1[start + 1:end + 1])
        location.latitude = jsonData["result"]["location"]["lat"]
        location.longitude = jsonData["result"]["location"]["lng"]
        print jsonData
    except:
        pass




    return location

curor = db['hotel'].find()
entity_list = []

for item in curor:
    entity_list.append(item)

for item in entity_list:
    #print "outer:"
    #print get_province_name(item["province"]) + get_city_name(item["city"]) + get_area_name(item["area_id"])
    gps = Location()
    gps.latitude = item["gps"]["latitude"]
    gps.longitude = item["gps"]["longitude"]
    if gps.latitude == 0:
        print item["hotel_address"]
        gps = get_location(item["hotel_address"].strip())

        db.hotel.update_one({"_id":ObjectId(item["_id"])},{"$set":{"gps": {"latitude":gps.latitude, "longitude":gps.longitude}}})

curor = db['restaurant'].find()
entity_list = []

for item in curor:
    entity_list.append(item)

for item in entity_list:
    #print "outer:"
    #print get_province_name(item["province"]) + get_city_name(item["city"]) + get_area_name(item["area_id"])
    gps = Location()
    gps.latitude = item["gps"]["latitude"]
    gps.longitude = item["gps"]["longitude"]
    if gps.latitude == 0:
        print item["restaurant_address"]
        gps = get_location(item["restaurant_address"].strip())

        db.restaurant.update_one({"_id":ObjectId(item["_id"])},{"$set":{"gps": {"latitude":gps.latitude, "longitude":gps.longitude}}})


curor = db['sights'].find()
entity_list = []

for item in curor:
    entity_list.append(item)

for item in entity_list:
    #print "outer:"
    #print get_province_name(item["province"]) + get_city_name(item["city"]) + get_area_name(item["area_id"])
    gps = Location()
    gps.latitude = item["gps"]["latitude"]
    gps.longitude = item["gps"]["longitude"]
    if gps.latitude == 0:
        print item["sights_address"]
        gps = get_location(item["sights_address"].strip())

        db.sights.update_one({"_id":ObjectId(item["_id"])},{"$set":{"gps": {"latitude":gps.latitude, "longitude":gps.longitude}}})