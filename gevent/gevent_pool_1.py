#!/usr/bin/ env python
# coding:utf-8
__author__ = 'Administrator'

import gevent
from gevent.pool import Pool
from gevent.pool import Group
import time
import requests

# 使用协程池可以显著提高并发性能
pool = Pool(2)

def down(url):
    print len(requests.get(url).content)

urls = ['http://www.maiziedu.com/', 'http://www.iqiyi.com/', 'http://www.baidu.com/', 'http://www.iteye.com/']

# group = Group()

for i in urls:
    pool.spawn(down, i)

t1 = time.time()
pool.join()
print 'use', time.time() - t1