#!/usr/bin/ env python
# coding:utf-8
__author__ = 'Administrator'

import gevent
from gevent.event import  Event, AsyncResult


evt = AsyncResult()
def setter():
    print u'i`m tearcher：linsten now!!!'
    gevent.sleep(5)
    print u'i`m tearcher：flish！！！'
    global evt
    evt.set('event message')

def waiter():
    print u'i`m student：listening'
    global evt, is_ok
    data = evt.get()
    print data
    print u'i`m student：hoho!!'

if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(setter)
        ,gevent.spawn(waiter)
        ,gevent.spawn(waiter)
    ])