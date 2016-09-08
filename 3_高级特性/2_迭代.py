# -*- coding: utf-8 -*-
__author__ = 'Administrator'

d = {'a':1,'b':2,'c':3}
# print d

# 只遍历key
for key in d:
    print key

# 只遍历val
for val in d.itervalues():
    print val

# 同时遍历key 和 val
for k, v in d.iteritems():
    print k,v

# 字符串也可迭代
for ch in 'ABC':
    print ch

# 判断一个对象是否可以迭代，True为可以迭代
from collections import Iterable

print isinstance('abc', Iterable) # True
print isinstance(123, Iterable) # False

# enumerate实现下标循环.下标从0开始
for i, val in enumerate('ABCDEFG'):
    print i,val

# 多个变量循环迭代
for x,y in [(1,2),(2,4),(3,9)]:
    print x,y