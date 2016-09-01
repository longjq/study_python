# -*- coding: utf-8 -*-
__author__ = 'Administrator'

# dict字典，使用{}代表，key值唯一
dict = {'Jay': 95, 'Andy': 128, 'Zhang': 99, 'Jay': 33}
print dict # jay:95被后面的jay:33给覆盖掉了
print dict['Jay']

dict['Andy'] = 88
print dict['Andy']

# 判断元素可以是否存在dict字典中
print 'Zhang' in dict

# key不存在就返回None或者自己指定的值
print dict.get('Andy123', 'is not exists')

# pop删除指定key，返回被删除的key的value值，第二个参数指定，不能存在删除key的时候，返回默认的值
# print dict.pop('Andy123', 'hahahahha') #不存在Andy123，就返回hahahahha
print dict.pop('Andy')
print dict

# dict内部存放的顺序和key放入的顺序是没有关系的。

# dict和list比较
# 1、查找和插入的速度极快，不会随着key的增加而增加。
# 2、需要占用大量的内存，内存浪费多。

# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

# set
# key不能重复，重复的元素会被过滤掉
s = set([1, 2, 3])
print s # set([1, 2, 3])返回的[1,2,3]，提示set中有三个元素，并不是list

# add添加元素
s.add('hello')
print s

# remove删除元素
s.remove('hello')
print s

# set可以做交集和并集的计算
s1 = set([1,2,3])
s2 = set([2,3,4])
print s1 & s2 # 交集运算
print s1 | s2 # 并集运算

# set和dict相同，不可放入对象，因为无法判别可变的对象是否相同

# 关于不可变对象
# str是一个不可变对象，对内容的指向已经定死了，如果对其操作方法返回的是操作后的结果而不是内容本身
# 例如 a.replace('a', 'A') 本身内容不变，返回操作后的新的结果值