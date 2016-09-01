# -*- coding: utf-8 -*-
__author__ = 'Administrator'

# 默认参数
def enroll(name, gender, age=6, city='Beijing'):
    print 'name:', name
    print 'gender:', gender
    print 'age:', age
    print 'city:', city

# enroll('Andy', 'man')

# 形参可以指定实参的指定数
enroll('Andy', 'man', city='Shanghai')

# list作为实参的坑！
# 如下，定义一个函数，初始化的时候，L已经被赋值为了空list
def add_end(L=[]):
    L.append('END')
    return L
'''
>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
'''
print add_end() # 第一次调用正常，因为是第一次添加END
print add_end() # 第二次调用异常，因为L指向[]，而[]得内容已经被改变了，因为[]是可变对象，就会异常
# 故默认参数必须指向不变对象

# 如下，多次调用，不会累计
def add_end_2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 可变参数
# numbers接收到的一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1,2,3) # 客户端代码

# 形参如果是一个list和tuple
nums = [1,2,3]
calc(*nums) # 如下传参
