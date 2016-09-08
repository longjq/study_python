#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

#from urllib import urlopen
#import re

#读取远程文件
#webpage = urlopen('http://www.163.com')
#text = webpage.read()
#print text


import urllib
urllib.urlretrieve('http://www.163.com', 'c:\\python_163.html')