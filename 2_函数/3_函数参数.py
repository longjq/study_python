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

# 形参如果是一个list和tuple，如下传参
nums = [1,2,3]
calc(*nums)

## 关键字参数
# 传入的0个或多个含参数名的参数，内部自动组装为dict
def person(name, age, **kw):
    print 'name',name,'age:',age,'kw:',kw

person('longjq',26,city='shenzhen') #必须带参数名
person('longjq',27,gender='M',job='Engineer') # 可以传入多个带参数名的参数

kw={'city':'beijing','job':'engineer'}
person('long',24,**kw) # 直接传入dict，可以自动匹配内部的dict

## 参数组合


