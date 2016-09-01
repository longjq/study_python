# -*- coding: utf-8 -*-
__author__ = 'Administrator'

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

y = -100
print -y
print my_abs(-33)

# 函数返回值None，直接写return就返回None，如果不写，也返回None，如果知道return true，就返回True

# pass 空函数
def nop():
    pass

if y >= 100:
    pass

# 参数检查
def my_abs_2(x):
    if not isinstance(x, (int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x;
    else:
        return -x;

# print my_abs_2('aaa')

# 返回多个值，返回的是tuple的值，可以多个值接收
def my_return_mutil():
    return '11', '22'

print my_return_mutil() # ('11', '22')

num1,num2 = my_return_mutil()
print num1 # 11
print num2 # 22