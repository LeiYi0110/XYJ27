# -*- coding: utf-8 -*-
__author__ = 'wanglei'

import mysql.connector
import json

from datetime import *

import os

#os.rename('/Users/wanglei/Downloads/image01.jpg', '/Users/wanglei/Documents/test/test.jpg')

import random
import string
import xlrd

import threading
print random.randint(1,50)

print random.randrange(0, 101, 2)

print random.random()
print round(random.uniform(8, 9),1)


def hello():
    print "hello, world"
    b = threading.Timer(0.5,hello)
    b.start()

hello()
#t = threading.Timer(0.5,hello)
#t.start()

'''
print random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')

print random.sample('zyxwvutsrqponmlkjihgfedcba',5)


book = xlrd.open_workbook('/Users/wanglei/Downloads/x2.xls')
sh = book.sheet_by_index(0)
for i in range(1,6):
    name = sh.cell_value(rowx=i, colx=2).strip()
    print( name)
    #print ord( name[len(name) - 1: len(name)])


import uuid

print uuid.uuid3(uuid.NAMESPACE_DNS, 'bcd')
print str(uuid.uuid3(uuid.NAMESPACE_DNS, '王雷.jp')) + 'OK'


x = ['9.qwqweq', '8.ntynty', '7.pbjfjerwk', '6.vhivjnoivjociv', '5.dwcsdgyjrmf', '4.pbkbojnpgfp']
y = sorted(x)
for item in y:
    print item
#print x
print ord('a')
'''