#!/usr/bin/ env python
# codeing:utf-8
__author__ = 'Administrator'
# greenlet 协程只能在同一个线程内运行，下面实例是在进程的主线程下运行的
from greenlet import greenlet
import threading

def t1():
    print threading.currentThread().getName()
    print '11'
    g2.switch()
    print '11_switch_after'
    g2.switch()

def t2():
    print threading.currentThread().getName()
    print '22'
    g1.switch()
    print '22_switch_after'
def new_th():
    g1.switch()


g1 = greenlet(t1)
# th = threading.Thread(target=new_th)
# th.start()
g2 = greenlet(t2)
g1.switch()

# th.join()