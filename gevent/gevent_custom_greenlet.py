#!/usr/bin/ env python
# codeing:utf-8
__author__ = 'Administrator'

import gevent

class MyGreenlet(gevent.Greenlet):
    def __init__(self, message, n, timeout):
        gevent.Greenlet.__init__(self)
        self.message = message
        self.n = n
        self.timeout = gevent.Timeout(timeout)

    def _run(self):
        self.timeout.start()
        print self.message
        gevent.sleep(self.n)

g1 = MyGreenlet('hello', 2, 1)
g1.start()
g1.join()
