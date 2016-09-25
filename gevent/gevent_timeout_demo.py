#!/usr/bin/ env python
# codeing:utf-8
__author__ = 'Administrator'

import gevent
from gevent import Timeout
time_to_wait=3

class TooLong(Exception):
    pass

try:
    with Timeout(time_to_wait, TooLong):
        gevent.sleep(4)
except Exception as e:
    print e