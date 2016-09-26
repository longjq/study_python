#!/usr/bin/ env python
# coding:utf-8
__author__ = 'Administrator'

import gevent
from gevent.pool import Pool
from gevent.lock import Semaphore
from gevent.lock import BoundedSemaphore

# 信号量，默认值为1，一次只能一个操作
# sem = Semaphore()
sem = BoundedSemaphore(2)
def worker1(n):
    sem.acquire()
    print 'worker %d acquire sem' % n
    gevent.sleep(0)
    sem.release()
    print 'worker %d release sem' % n

# 使用with语法实现一次操作一个
def worker2(n):
    with sem:
        print 'worker %d acquire sem' % n
        gevent.sleep(0)
    print 'worker %d release sem' % n


pool = Pool()
pool.map(worker1, xrange(0, 5))
# pool.map(worker2, xrange(0, 5))