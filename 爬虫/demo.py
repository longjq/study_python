#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import urllib2

response = urllib2.urlopen('http://www.baidu.com')

print response.read()