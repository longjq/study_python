#!/usr/bin/ env python
# codeing:utf-8
__author__ = 'Administrator'
from threading import Thread
import Queue
import redis
import time

# 在逻辑线程中处理io请求并处理数据
def handle_callback(rs):
    print 'callback: ', rs

class SetData:
    def __init__(self, key, value, handle):
        self.key = key
        self.value = value
        self.handle = handle

class RedisAsyncHandle(Thread):
    queue = Queue.Queue(maxsize=1024)
    r = redis.Redis(host='localhost', port=6379, db=0)

    def send_set_cmd(self, key, value):
        set_data = SetData(key, value, handle_callback)
        self.queue.put(set_data)

    def run(self):
        while True:
            while not self.queue.empty():
                item = self.queue.get()
                print 'get item'
                rs = self.r.set(item.key, item.value)
                item.handle(rs)
            time.sleep(0.1)

handle = RedisAsyncHandle()
handle.start()

handle.send_set_cmd('name1', 'longjq1')
handle.send_set_cmd('name2', 'longjq2')
handle.send_set_cmd('name3', 'longjq3')
handle.join()