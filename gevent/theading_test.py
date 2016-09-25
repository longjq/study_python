#!/usr/bin/ env python
# codeing:utf-8
__author__ = 'Administrator'

import threading

def run_test():
    print threading.currentThread().getName()
    for i in range(10):
        print i

print threading.currentThread().getName()
thead1 = threading.Thread(target=run_test)
thead1.start()
thead1.join()
