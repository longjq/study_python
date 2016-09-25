#!/usr/bin/ env python
# codeing:utf-8
__author__ = 'Administrator'
from gevent import Greenlet
from gevent import spawn
from gevent import joinall
from gevent import sleep as g_sleep
import time

# def run_in_greenlet(n):
#     print time.time()
#     print 'running success!', n
#
# g1 = Greenlet(run_in_greenlet,33333)
# print time.time()
# # g1.start()
# g1.start_later(1)
# g1.join()


# def run_in_greenlet():
#     print time.time()
#     print 'running success!'
#
# g1 = spawn(run_in_greenlet)
# print time.time()
# g1.join()



# def run_in_greenlet1():
#     print time.time()
#     print 'running success!__1'
# def run_in_greenlet2():
#     print time.time()
#     print 'running success!__2'
#
# g1 = spawn(run_in_greenlet1)
# g2 = spawn(run_in_greenlet2)
# print time.time()
# g2.join()
# g1.join()




# def run_in_greenlet1():
#     print time.time()
#     print 'running success!__1'
# def run_in_greenlet2():
#     print time.time()
#     print 'running success!__2'
#
# g1 = spawn(run_in_greenlet1)
# g2 = spawn(run_in_greenlet2)
# print time.time()
# glist = [g1, g2]
# joinall(glist)



def run_in_greenlet1():
    print 'running success!__1'
    g_sleep(0) # gevent中使用gevent.sleep(0)来切换，以代替greenlet.switch()方法，实现切换协程
    print 'running success!__1.1'

def run_in_greenlet2():
    print 'running success!__2'
    g_sleep(0)
    print 'running success!__2.2'





print time.time()
joinall([spawn(run_in_greenlet1), spawn(run_in_greenlet2)])