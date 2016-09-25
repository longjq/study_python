#!/usr/bin/ env python
# codeing:utf-8
__author__ = 'Administrator'

import gevent

def win():
    return  'hello world!'
def fail():
    raise Exception('you are failing')

# winner = gevent.Greenlet(win)
# winner.start()
# print winner.started


# winner = gevent.spawn(win)
# gevent.joinall([winner,])
# print winner.value


winner = gevent.spawn(win)
loser = gevent.spawn(fail)

try:
    gevent.joinall([winner, loser])
except Exception as e:
    print e
print loser.ready()
print loser.successful()
print loser.exception
