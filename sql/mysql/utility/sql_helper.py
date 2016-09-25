#!/usr/bin/ env python
# codeing:utf-8
__author__ = 'Administrator'


import mysql.connector

class MySqlHelper(object):

    def __init__(self):
        pass

    def Get_Dict(self, sql, params):
        conn =mysql.connector.con
