#!/usr/bin/ env python
# codeing:utf-8
__author__ = 'Administrator'

import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='demo')
cursor = conn.cursor()

cursor.execute('select * from users')

values = cursor.fetchall()
print values

cursor.close()

conn.close()
# 你好啊，你说什么，呵呵呵呵