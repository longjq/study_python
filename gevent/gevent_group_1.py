#!/usr/bin/ env python
# coding:utf-8
__author__ = 'Administrator'

import gevent
from gevent.pool import Group

group = Group()

def talk(msg):
    for i in xrange(3):
        print i,msg

g1 = gevent.spawn(talk, 'bar')
g2 = gevent.spawn(talk, 'foo')

group.add(g1)
group.add(g2)

group.join()