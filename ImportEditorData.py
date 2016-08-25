# -*- coding: utf8 -*-
__author__ = 'wanglei'
import xlrd

import sys,os,json,httplib

import mysql.connector

import pymongo

import types

from datetime import *

import uuid

import urllib



'''
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
'''

#cnxXYJ = mysql.connector.connect(user='tour', password='Tour@2015', host='120.25.207.34', database='tour')

mysql_user = 'tour'
mysql_pwd = 'Tour@2015'
mysql_host = '120.25.207.34'
mysql_connect_database = 'tour'

con = pymongo.MongoClient("120.25.207.34", 27017)
db = con.xyj
db.authenticate("xyj", "xyj88283088")

host = "http://www.xiangyouji.com.cn:3000"


class Location:
    def __init__(self):
        self.latitude = 0.0
        self.longitude = 0.0

class Entity:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.phone = ""
        self.desc = ""
        self.imageList = []
        self.gps = Location()
        self.area_id = 0
        self.province = 0
        self.entity_type = 0
        self.city = 0


def import_provice_data(path,province_name,editor):
    #path = '/Users/wanglei/Desktop/山东'
    province_id = get_province_id(province_name)
    unPath = path #unicode(path, "utf8")
    for city in os.listdir(unPath):
        pathCity = unPath + '/' + city

        if os.path.isdir(pathCity):
            #print city
            city_id = get_city_id(city)
            if city_id == 0:
                add_error(editor,pathCity,"城市名字输入不对")
            for area in os.listdir(pathCity):

                pathArea = pathCity + '/' + area
                if os.path.isdir(pathArea):
                    #print '     ' + area
                    area_id = get_area_id(area)
                    if area_id == 0:
                        add_error(editor,pathArea,"地区名字输入不对")
                    for super_entity_type in os.listdir(pathArea):
                        pathSuperEntityType = pathArea + '/' + super_entity_type
                        if os.path.isdir(pathSuperEntityType) and super_entity_type == u"景点":
                            #print '         ' + super_entity_type
                            for entity_type in os.listdir(pathSuperEntityType):
                                pathEntityType = pathSuperEntityType + '/' + entity_type
                                if os.path.isdir(pathEntityType):
                                    #entityList = []
                                    entityDic = {}
                                    #print(entity_type)
                                    entity_type_id = get_entity_type_id(entity_type)
                                    for generalItem in os.listdir(pathEntityType):
                                        pathGeneralItem = pathEntityType + '/' + generalItem
                                        if os.path.isfile(pathGeneralItem) and (generalItem.endswith('.xlsx') or generalItem.endswith('.xls')):
                                            print pathGeneralItem
                                            try:
                                                book = xlrd.open_workbook(pathGeneralItem)

                                                sh = book.sheet_by_index(0)
                                                for rx in range(1, sh.nrows):
                                                    try:
                                                        entity = Entity()
                                                        entity.name = sh.cell_value(rowx=rx, colx=2).strip()
                                                        entity.address = sh.cell_value(rowx=rx, colx=5)

                                                        phone = sh.cell_value(rowx=rx, colx=6)
                                                        entity.phone = str(phone)

                                                        if len(entity.phone) == 0:
                                                            phone = sh.cell_value(rowx=rx, colx=1)
                                                            entity.phone = str(phone)

                                                        '''
                                                        if type(phone) is types.StringType:
                                                            entity.phone = phone
                                                        elif type(phone) is types.FloatType or type(phone) is types.IntType:
                                                            entity.phone = str(phone)
                                                        '''

                                                        '''
                                                        if len(entity.phone) == 0:
                                                            phone = sh.cell_value(rowx=rx, colx=1)
                                                            if type(phone) is types.StringType:
                                                                entity.phone = phone
                                                            elif type(phone) is types.FloatType or type(phone) is types.IntType:
                                                                entity.phone = str(phone)
                                                        if len(entity.phone) > 0:
                                                            entity.phone = str(long((float(entity.phone))))
                                                        '''

                                                        db.phoneData.insert({"entity_name":entity.name,"phone":entity.phone})
                                                        entity.gps = get_location(entity.address)
                                                        entity.area_id = area_id
                                                        entity.province = province_id
                                                        entity.entity_type = entity_type_id
                                                        entity.city = city_id
                                                #print entity.name, entity.address
                                                #entityList.append(entity)
                                                        entityDic[entity.name] = entity
                                                    except:
                                                        add_error(editor,pathImageDescItem, 'excel格式不对')
                                                        pass
                                            except:
                                                pass




                                    for generalItem in os.listdir(pathEntityType):
                                        pathImageAndDescItem = pathEntityType + '/' + generalItem
                                        if os.path.isdir(pathImageAndDescItem):
                                            for imageDescItem in os.listdir(pathImageAndDescItem):
                                                pathImageDescItem = pathImageAndDescItem + '/' + imageDescItem
                                                if os.path.isdir(pathImageDescItem):
                                                    order = 0
                                                    dirList = sorted(os.listdir(pathImageDescItem))
                                                    for imageItem in dirList:
                                                        if not imageItem.startswith('.'):
                                                            #print imageItem
                                                            order = order + 1
                                                            tmp_array = imageItem.split('.')
                                                            end_fix = tmp_array[len(tmp_array) - 1]
                                                            if end_fix == 'db':
                                                                continue
                                                            image_item_name = str(uuid.uuid3(uuid.NAMESPACE_DNS, (imageDescItem + imageItem).encode('utf8'))) + '.' + end_fix
                                                            imageListItem = {"url":host + "/" + image_item_name, "order":order,"create_time":datetime.now(), "update_time":datetime.now()}
                                                            try:
                                                                entityDic[imageDescItem].imageList.append(imageListItem)
                                                            except:
                                                                #add_error(editor,pathImageDescItem + '/' + imageItem, '图片没有出现在excel')
                                                                add_error(editor,pathImageDescItem, '图片没有出现在excel')
                                                                pass
                                                            try:
                                                                print imageItem

                                                                #os.rename(pathImageDescItem + '/' + imageItem, '/opt/productImage/' + image_item_name )

                                                            except:
                                                                pass


                                                elif os.path.isfile(pathImageDescItem) and imageDescItem.endswith('txt'):
                                                    errorItem = imageDescItem
                                                    imageDescItem = imageDescItem[0: len(imageDescItem) - 3].strip()
                                                    imageDescItem = imageDescItem[0: len(imageDescItem) - 1].strip()
                                                    #print "image desc item:"
                                                    #print imageDescItem

                                                    f = open(pathImageDescItem)
                                                    line = f.readline()
                                                    resultLine = ""
                                                    while line:
                                                        resultLine += line.decode('gbk','ignore')
                                                        line = f.readline()
                                                    try:
                                                        entityDic[imageDescItem].desc = resultLine
                                                        #print resultLine
                                                    except:
                                                        add_error(editor, pathImageDescItem, '描述没有出现在excel')
                                                        pass


                                    for key in entityDic.keys():
                                        print "add " + key
                                        #db.phoneData.insert({"entity_name":entityDic[key]})
                                        #add_data_to_mongodb(entityDic[key])






def get_province_id(province_name):

    province_id = 0
    cnxXYJ = mysql.connector.connect(user=mysql_user, password=mysql_pwd, host=mysql_host, database=mysql_connect_database)

    cursorXYJ = cnxXYJ.cursor()
    cursorXYJ.execute("select id from area_province where name = '" + province_name + "'")
    for item in cursorXYJ:
        province_id = item[0]
    cnxXYJ.close()
    return province_id



def get_city_id(city_name):
    city_id = 0
    cnxXYJ = mysql.connector.connect(user=mysql_user, password=mysql_pwd, host=mysql_host, database=mysql_connect_database)

    cursorXYJ = cnxXYJ.cursor()
    cursorXYJ.execute("select id from area_city where name = '" + city_name + "'")
    for item in cursorXYJ:
        city_id = item[0]
        break
    cnxXYJ.close()
    return city_id


def get_area_id(area_name):
    area_id = 0
    cnxXYJ = mysql.connector.connect(user=mysql_user, password=mysql_pwd, host=mysql_host, database=mysql_connect_database)

    cursorXYJ = cnxXYJ.cursor()
    cursorXYJ.execute("select id from area_county where name = '" + area_name + "'")
    for item in cursorXYJ:
        area_id = item[0]


    cnxXYJ.close()
    return area_id


def get_entity_type_id(entity_name):
    if entity_name == u"农家乐":
        return 2
    elif entity_name == u"山庄酒店":
        return 1
    elif entity_name == u"乡村景点":
        return 3
    return 0


def add_error(error_editor, path, error_name):
    cnxXYJ = mysql.connector.connect(user=mysql_user, password=mysql_pwd, host=mysql_host, database=mysql_connect_database)

    cursorXYJ = cnxXYJ.cursor()
    data_error = {
            'editor': error_editor,
            'path': path,
            'error_name': error_name
            }

    insert_error = ("INSERT INTO editor_error "
              "(editor,path,error_name) "
              "VALUES (%(editor)s,%(path)s,%(error_name)s)")
    cursorXYJ.execute(insert_error, data_error)
    cnxXYJ.commit()
    cnxXYJ.close()

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

def add_data_to_mongodb(entity):
    cover = ""
    if len(entity.imageList) > 0:
        cover = entity.imageList[0]["url"]

    '''
    db['common_data'].insert({"area_id": entity.area_id, "name": entity.name,
                              "address": entity.address,
                              "phone": entity.phone, "gps": {"latitude":entity.gps.latitude, "longitude":entity.gps.longitude}, "cover": cover,
                              "entity_id": "", "entity_type": entity.entity_type, "province": entity.province, "images": entity.imageList, "city":entity.city, "collection_count": 0, "comment_count": 0})
    '''

    if entity.entity_type == 1:
        db.hotel.insert({"shop_id": "", "hotel_name": entity.name, "hotel_address": entity.address, "hotel_desc": entity.desc,
                     "hotel_telephone": entity.phone, "city_id": entity.city, "area_id": entity.area_id, "province": entity.province,
                     "gps": {"longitude": entity.gps.longitude, "latitude": entity.gps.latitude}, "create_time": datetime.now(),
                     "update_time": datetime.now(), "lowest_price": 0.0, "room_value": 0.0, "location_value": 0.0,
                     "service_value": 0.0, "avg_price": 0.0, "star_count": 0.0, "cover": cover, "images": entity.imageList, "city":entity.city, "collection_count": 0, "comment_count": 0})
    elif entity.entity_type == 2:
        db.restaurant.insert({"shop_id": "", "restaurant_name": entity.name, "restaurant_address": entity.address,"restaurant_desc":entity.desc,
                     "restaurant_telephone": entity.phone, "city_id": entity.city, "area_id": entity.area_id, "province": entity.province,
                     "gps": {"longitude": entity.gps.longitude, "latitude": entity.gps.latitude}, "create_time": datetime.now(),
                     "update_time": datetime.now(), "lowest_price": 0.0, "taste_value": 0.0, "environment_value": 0.0,
                     "service_value": 0.0, "avg_price": 0.0, "star_count": 0.0, "cover": cover, "images": entity.imageList, "city":entity.city, "collection_count": 0, "comment_count": 0})
    elif entity.entity_type == 3:
        db.sights.insert({"shop_id": "", "sights_name": entity.name, "sights_address": entity.address,"sights_desc":entity.desc,
                     "sights_telephone": entity.phone, "city_id": entity.city, "area_id": entity.area_id, "province": entity.province,
                     "gps": {"longitude": entity.gps.longitude, "latitude": entity.gps.latitude}, "create_time": datetime.now(),
                     "update_time": datetime.now(), "lowest_price": 0.0, "beautiful_value": 0.0, "save_mny_value": 0.0,
                     "service_value": 0.0, "avg_price": 0.0, "star_count": 0.0, "cover": cover, "images": entity.imageList, "city":entity.city, "collection_count": 0, "comment_count": 0})




#import_provice_data('/Users/wanglei/Desktop/山东', "山东", "王雷")

#path = '/opt/EditorData'

editor_root_path = unicode("/opt/EditorData", "utf8")
#editor_root_path = unicode("/opt/EditorFeng", "utf8")
for editor in os.listdir(editor_root_path):
    #import_provice_data(editor_path + '/' + editor, "山东", editor)
    editor_path = editor_root_path + '/' + editor

    if os.path.isdir(editor_path):
        for province in os.listdir(editor_path):
            province_path = editor_path + '/' + province
            if os.path.isdir(province_path):
                import_provice_data(province_path, province, editor)




print get_province_id("山东省")
print get_city_id("深圳市")
print get_area_id("福田区")