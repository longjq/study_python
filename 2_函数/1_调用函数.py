# -*- coding: utf-8 -*-
__author__ = 'Administrator'
# abs(x) 绝对值函数
print abs(-13)

# cmp(x, y) 比较函数，x<y返回-1，x==y返回0，x>y返回1
print cmp(1, 3)   # -1
print cmp(33, 33) # 0
print cmp(14, 4)  # 1

# 类型转换
print int('123') # 123
print int(12.34) # 12
print float('123.4677') # 123.4677
print str(1.23) # '1.23'
print unicode(100) #u'100'
print bool(1) # True
print bool('') # False

# 支持变量指向函数的引用
a = abs
print a(-33); # 33