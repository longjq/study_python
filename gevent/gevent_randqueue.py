#!/usr/bin/ env python
# coding:utf-8
__author__ = 'Administrator'

import gevent
import random
from gevent.queue import Queue

class RandQueue(Queue):
    def _init(self, maxsize, items=None):
        self.queue = []

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.pop(random.randint(0, len(self.queue) - 1))

q = RandQueue(10)

for i in xrange(10):
    q.put(i)

print q

for i in xrange(10):
    print q.get()