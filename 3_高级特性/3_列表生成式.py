# -*- coding: utf-8 -*-
__author__ = 'Administrator'

# 列表生成式，创建list的语法糖
print [x * x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 加上if判断的生成list
print [x * x for x in range(1,11) if x % 2 == 0]

# 嵌套循环
print [m + n for m in 'ABC' for n in 'XYZ']

# 列出当前目录下的所有文件和目录
import os
print [d for d in os.listdir('.')]

# 列表生成式，key=value变量操作
d = {'x':'A','y':'B','z':'C'}
print [k + '=' + v for k,v in d.iteritems()]

L = ['HELLO','WORLD','IBM','APPLE']
print [s.lower() for s in L]

L2 = ['HELLO','WORLD','IBM',19,None]
print [isinstance(s,str) and s.lower() or s for s in L2]