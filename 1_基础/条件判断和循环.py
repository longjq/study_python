# -*- coding: utf-8 -*-
__author__ = 'Administrator'

# if语句的使用
age = 30
if age >= 20:
    print age, ' >= 20'
elif age >= 10:
    print age, ' >= 10'
else:
    print 'age is ', age

# x即if里的表达式结果不是0、''、[]就为True
x = ''
if x:
    print 'x is not 0 or empty or '' or [] or false'

# for in 循环
sum = 0
for x in range(1, 6):
    sum = sum + x
print sum

# 读取用户输入raw_input
birth = raw_input('birth:')
print 'your input birth is ', birth

# int 类型检查，如果不是int类型就报错！！！
birth = int(raw_input('birth:'))
print 'your input birth is validate, the number is ',birth