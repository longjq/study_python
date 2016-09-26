#!/usr/bin/ env python
# coding:utf-8
__author__ = 'Administrator'

import gevent
from gevent.pool import Group

group = Group()

def group_map(n):
    print n
    print 'size of group %s' % len(group)
    print 'hello from Greenlet %s' % id(gevent.getcurrent())

# 一次性装载3个协程并马上运行
# group.map(group_map, xrange(3))

# 延迟运行，先装载，迭代的时候再真正的执行
# imap_data = group.imap(group_map, xrange(3))
# for i in imap_data:
#     print i

# 延迟运行，先装载，迭代的时候再真正的执行，不是顺序执行
imap_data = group.imap_unordered(group_map, xrange(3))
for i in imap_data:
    print i