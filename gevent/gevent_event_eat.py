#!/usr/bin/ env python
# coding:utf-8
__author__ = 'Administrator'

import gevent
from gevent.event import AsyncResult

diet_dict= {'ljq':'rice','kate':'bread'}

evt = AsyncResult()

def setter():
    print 'begin cook'
    gevent.sleep(4)
    print 'cook over'
    evt.set('bread')

def waiter(name):
    print name,'begin to wait'
    diet = diet_dict[name]
    if not diet:
        print 'error'
        return
    got_diet = evt.wait()
    if got_diet == diet:
        print '%s got right diet %s so happy' %(name, got_diet)
    else:
        print '%s not right diet %s so bad' % (name, diet)

if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter, 'ljq'),
        gevent.spawn(waiter, 'kate')]
    )