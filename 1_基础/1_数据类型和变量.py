# -*- coding: utf-8 -*-
__author__ = 'Administrator'

# 不解析字符串r
print r'\\\t\\'

# 多行，加上r不解析常见转移符
print r'''
line1
line2_1\tline2_2
line3
'''

# 简单ifpanda
age = 2000
if  age >= 18:
    print 'adult'
else:
    print 'teenager'

# 常量，人为大写，貌似python没有常量的概念
PI = 3.14159265359

# 关于除法，如果需要得到小数，直接在除数上加上.0即可
print 10.0 / 3