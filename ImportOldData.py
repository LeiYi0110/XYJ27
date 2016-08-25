__author__ = 'wanglei'

import mysql.connector
import json

from datetime import *


print "hello new debian"





cnxTour = mysql.connector.connect(user='tour', password='Tour@2015',
                              host='120.25.207.34',
                              database='tour')

cnxXYJ = mysql.connector.connect(user='tour', password='Tour@2015', host='120.25.207.34', database='xyj_common_dev')


cursorTour = cnxTour.cursor()
cursorXYJ = cnxXYJ.cursor()
cursorTour.execute('select * from tour_attractions where type = 1')






def insert_image_data(image_address, entity_type, i_entity_id, order_no):

    print insert

    data_image = {
        'image_address': image_address,
        'entity_type': entity_type,
        "entity_id": i_entity_id,
        "order_no": order_no
    }

    add_image = ("INSERT INTO entity_image "
              "(image_address,entity_type,entity_id,order_no) "
              "VALUES (%(image_address)s,%(entity_type)s,%(entity_id)s,%(order_no)s)")

    cursorXYJ.execute(add_image, data_image)


for tourItem in cursorTour:
    try:
        tour_id = str(tourItem[0])
        cursorXYJ.execute('select id from sights where tour_id = ' + tour_id)
        print tourItem[7]

        entity_id = 0
        for item in cursorXYJ:
            entity_id = item[0]
        print entity_id
        print tourItem[8]
        i = 0

        entity_type = 3
        data_image = {
            'image_address': tourItem[7],
            'entity_type': entity_type,
            "entity_id": entity_id,
            "order_no": i
        }

        add_image = ("INSERT INTO entity_image "
                  "(image_address,entity_type,entity_id,order_no) "
                  "VALUES (%(image_address)s,%(entity_type)s,%(entity_id)s,%(order_no)s)")

        cover = str(tourItem[7])

        if len(cover) != 0 and (not cover.endswith('.db')):
            cursorXYJ.execute(add_image, data_image)





        otherImages = json.loads(tourItem[8])


        for image in otherImages:
            i = i + 1
            data_image = {
                'image_address': image['url'],
                'entity_type': entity_type,
                "entity_id": entity_id,
                "order_no": i
            }
            url = str(image['url'])
            if len(url) != 0 and (not url.endswith('.db')):
                cursorXYJ.execute(add_image, data_image)
        cnxXYJ.commit()
    except:
        pass





cnxTour.close()
cnxXYJ.close()













