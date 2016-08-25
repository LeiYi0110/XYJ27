__author__ = 'wanglei'



import mysql.connector
import json
import pymongo

from datetime import *


print "hello new debian"

con = pymongo.MongoClient("120.25.207.34", 27017)
db = con.xyj
db.authenticate("xyj", "xyj88283088")
#print db.test.find_one({})

hotelList = []


cnxXYJ = mysql.connector.connect(user='tour', password='Tour@2015', host='120.25.207.34', database='xyj_common_dev')


cursorXYJ = cnxXYJ.cursor()

cursorXYJ.execute('select * from hotel')
hotelList = []




i = 0
for hotelItem in cursorXYJ:
    hotelList.append(hotelItem)

for hotelItem in hotelList:
    print hotelItem
    '''
    db.hotel.insert({"shop_id": "", "hotel_name": hotelItem[2], "hotel_desc": hotelItem[5], "hotel_address": hotelItem[6],
                     "hotel_telephone": hotelItem[7], "city_id": hotelItem[14], "area_id": hotelItem[15], "province": hotelItem[16],
                     "city": hotelItem[17], "town": hotelItem[18], "village": hotelItem[19], "tour_id":hotelItem[22],
                     "gps": {"longitude": hotelItem[3], "latitude": hotelItem[4]}, "create_time": datetime.now(),
                     "update_time": datetime.now(), "lowest_price": 0.0, "room_value": 0.0, "location_value": 0.0,
                     "service_value": 0.0, "avg_price":0.0, "star_count": 0.0})
    '''

    cursorXYJ.execute('select * from entity_image where entity_type = 1 and entity_id = ' + str(hotelItem[0]))
    imageList = []
    cover = ""
    for imageItem in cursorXYJ:
        imageList.append({"url":imageItem[4], "order_no":imageItem[3], "create_time":datetime.now(), "update_time":datetime.now()})

    if len(imageList) > 0:
        cover = imageList[0]["url"]
    '''
    db.hotel.insert({"shop_id": "", "hotel_name": hotelItem[2], "hotel_desc": hotelItem[5], "hotel_address": hotelItem[6],
                     "hotel_telephone": hotelItem[7], "city_id": hotelItem[14], "area_id": hotelItem[15], "province": hotelItem[16],
                     "city": hotelItem[17], "town": hotelItem[18], "village": hotelItem[19], "tour_id":hotelItem[22],
                     "gps": {"longitude": hotelItem[3], "latitude": hotelItem[4]}, "create_time": datetime.now(),
                     "update_time": datetime.now(), "lowest_price": 0.0, "room_value": 0.0, "location_value": 0.0,
                     "service_value": 0.0, "avg_price": 0.0, "star_count": 0.0, "cover": cover, "images": imageList})
    '''
    db.hotel.insert({"shop_id": "", "hotel_name": hotelItem[2], "hotel_address": hotelItem[6], "hotel_desc": "",
                     "hotel_telephone": hotelItem[7], "city_id": hotelItem[14], "area_id": hotelItem[15], "province": hotelItem[16],
                     "city": hotelItem[17], "town": hotelItem[18], "village": hotelItem[19], "tour_id":hotelItem[22],
                     "gps": {"longitude": hotelItem[3], "latitude": hotelItem[4]}, "create_time": datetime.now(),
                     "update_time": datetime.now(), "lowest_price": 0.0, "room_value": 0.0, "location_value": 0.0,
                     "service_value": 0.0, "avg_price": 0.0, "star_count": 0.0, "cover": cover, "images": imageList})

cnxXYJ.close()




'''

    stockList = []

    for stockItem in data_array:
        stockData = stockItem.split(',')
        stockList.append({"code":stockData[1],"stockName":stockData[2], "currentPrice":stockData[5],"quickIncrease":stockData[13],"closePrice":stockData[3],"openPrice":stockData[4],"lowPrice":stockData[7],"increaseRate":stockData[11],"dealAmt":stockData[9],"dealMny":stockData[8],"increaseMny":stockData[10],"highPrice":stockData[6],"fiveMinIncreaseRate":stockData[21],"stockDataTime":stockData[28],"insertTime":datetime.now()})




    #insertData = json.dumps(stockList)

    db.cdb.insert(stockList)
'''

#testCollection = db.test














