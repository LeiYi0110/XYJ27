# -*- coding: utf8 -*-
__author__ = 'wanglei'
import xlrd

import sys,os,json,httplib

import mysql.connector

import pymongo

import types

from datetime import *

import uuid

#path = "/Users/wanglei/Desktop/上海市/上海市/上海市主题数据导入.xls"

con = pymongo.MongoClient("120.25.207.34", 27017)
db = con.xyj
db.authenticate("xyj", "xyj88283088")

host = "http://www.xiangyouji.com.cn:3000/"

mysql_user = 'tour'
mysql_pwd = 'Tour@2015'
mysql_host = '120.25.207.34'
mysql_connect_database = 'tour'


class Theme:
    def __init__(self):
        self.cover = ""
        self.title = ""
        self.entities = []
        self.order = 0
        self.province = 0
        self.gps = Location()

class Entity:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.phone = ""
        self.imageList = []
        self.gps = Location()
        self.area_id = 0
        self.province = 0
        self.entity_type = 0
        self.cover = ""
        self.entity_id = ""


class Location:
    def __init__(self):
        self.latitude = 0.0
        self.longitude = 0.0

class Province:
    def __init__(self):
        self.province_id = 0
        self.province_name = ""
        self.gps = Location()


path = "/Users/wanglei/Desktop/上海市/上海市"
path = unicode(path,"utf8")




def read_excel(excel_file_name,folder_path,province_collect):
    try:
        book = xlrd.open_workbook(folder_path + "/" + excel_file_name)
        #print book.sheet_names()

        for i in range(0,len(book.sheet_names())):
            print book.sheet_names()[i]
            theme = Theme()
            theme.title = book.sheet_names()[i]
            cover_image_name = get_file_by_name(folder_path,theme.title)

            #print "cover_image_name: " + cover_image_name
            if len(cover_image_name) == 0:
                print "folder_path: " + folder_path
                print theme.title


            cover_path = generate_image_file_name(folder_path + theme.title,cover_image_name)
            theme.cover = host + cover_path
            #os.rename(folder_path + '/' + cover_image_name, '/opt/productImage/' + cover_path )
            theme.order = i
            theme.province = province_collect.province_id
            theme.gps = province_collect.gps
            sh = book.sheet_by_index(i)

            for j in range(1,sh.nrows):

                entity_name = sh.cell_value(rowx=j, colx=0).strip()
                #print entity_name
                image_name = sh.cell_value(rowx=j, colx=1).strip()

                try:
                    entity = get_entity_by_name(entity_name)
                    entity.cover = host + generate_image_file_name(entity_name,image_name)
                    theme.entities.append({"url":entity.cover, "order":i, "entity_type":entity.entity_type, "entity_id":entity.entity_id, "images": entity.imageList, "gps":entity.gps, "collected_count":0,"name":entity_name})
                except:
                    pass

            #db.theme.insert({"cover":theme.cover, "title":theme.title, "entities":theme.entities, "order": theme.order, "province":theme.province,"gps":theme.gps})
            db.theme.insert({"cover":theme.cover, "title":theme.title, "entities":theme.entities, "order": theme.order, "province":theme.province, "gps":{"latitude":theme.gps.latitude, "longitude":theme.gps.longitude}})

            '''
            if province_id == 19:
                print theme.title
                print theme.cover
            '''
            #print theme.cover
            #if province_id == 19:


    except:
        #print folder_path + "/" + excel_file_name
        pass
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

def generate_image_file_name(entity_name,image_name):
    tmp_array = image_name.split('.')
    end_fix = tmp_array[len(tmp_array) - 1]

    return str(uuid.uuid3(uuid.NAMESPACE_DNS, (entity_name + image_name).encode('utf8'))) + '.' + end_fix

def get_file_by_name(file_path, file_name):
    for item in os.listdir(file_path):
        item_path = file_path + "/" + item
        #print item_path
        #print file_name
        if os.path.isfile(item_path) and item.startswith(file_name):
            return item

    return ""

def get_location(address):

    #print address
    conn = httplib.HTTPConnection("api.map.baidu.com")
    #conn.request("GET","/geocoder/v2/?address=青岛市市南区观象二路21号（观象山公园中心）&output=json&ak=aez4EuqcDUoOF7oKwPFsyijv&callback=showLocation")
    url = "/geocoder/v2/?address=" + address.encode('utf8') + "&output=json&ak=aez4EuqcDUoOF7oKwPFsyijv&callback=showLocation"
    conn.request("GET",url)
    r1 = conn.getresponse()
    #print(r1.status, r1.reason)
    data1 = r1.read()
    #print data1
    start = data1.find('({')
    end = data1.find('})')

    location = Location()
    try:
        jsonData = json.loads(data1[start + 1:end + 1])
        location.latitude = jsonData["result"]["location"]["lat"]
        location.longitude = jsonData["result"]["location"]["lng"]
    except:
        pass




    return location

def get_province(province_name):

    province_id = 0
    cnxXYJ = mysql.connector.connect(user=mysql_user, password=mysql_pwd, host=mysql_host, database=mysql_connect_database)

    cursorXYJ = cnxXYJ.cursor()
    cursorXYJ.execute("select id from area_province where name = '" + province_name + "'")
    for item in cursorXYJ:
        province_id = item[0]
    cnxXYJ.close()

    province_get = Province()
    province_get.province_id = province_id
    province_get.province_name = province_name
    province_get.gps = get_location(province_name)

    print province_name
    print province_get.gps

    return province_get


editor_root_path = unicode("/opt/EditorData", "utf8")

'''
for editor in os.listdir(editor_root_path):
    editor_path = editor_root_path + '/' + editor
    if os.path.isdir(editor_path):
        for province in os.listdir(editor_path):
            province_path = editor_path + '/' + province
            if os.path.isdir(province_path):
                for item in os.listdir(province_path):
                    item_path = province_path + '/' + item
                    if os.path.isfile(item_path) and (item.endswith('.xlsx') or item.endswith('.xls')):
                        read_excel(item,province_path,get_province(province))
                        break
'''

for editor in os.listdir(editor_root_path):
    editor_path = editor_root_path + '/' + editor
    if os.path.isdir(editor_path):
        for province in os.listdir(editor_path):
            province_path = editor_path + '/' + province
            if os.path.isdir(province_path):
                for item in os.listdir(province_path):
                    item_path = province_path + '/' + item
                    province_obj = get_province(province)
                    if province_obj.province_id == 1 or province_obj.province_id == 2 or province_obj.province_id == 9 or province_obj.province_id == 22:
                        for city_item in os.listdir(item_path):
                            city_item_path = item_path + '/' + city_item
                            if os.path.isfile(city_item_path) and (city_item.endswith('.xlsx') or city_item.endswith('.xls')):
                                read_excel(city_item,item_path,get_province(province))
                                break









