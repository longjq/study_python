#!/usr/bin/ env python
# codeing:utf-8
__author__ = 'Administrator'

import gevent
import time
#
# def wait():
#     gevent.sleep(4)
#
# wait_time = 2
# tiemout = gevent.Timeout(2)
# tiemout.start()
#
# try:
#     gevent.spawn(wait())
# except gevent.Timeout:
#     print 'timeout!!!'


def wait():
    gevent.sleep(4)
wait_time = 2
class Toolong(Exception):
    pass
with gevent.Timeout(wait_time, Toolong):
    gevent.sleep(3)
