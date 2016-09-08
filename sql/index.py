#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='demo', use_unicode=True)

cursor = conn.cursor()
cursor.execute('select * from user_events')
values = cursor.fetchall()
print values