# -*- coding: utf-8 -*-
__author__ = 'Administrator'

L = range(10) # 生成到9截止，比给定的值要小一位
print L
print L[:10]
print L

# 取前三个参数，从0开始，到3截止，即0，1，2不包含3
print L[0:3]
# 简写
print L[:3]

# 从末尾取
print L[-2:] # 从倒数第二位数字，往后取，得到8,9
print L[-2:-1] # 从倒数第二位数字往后取一个值，得到8

# 从中间取
print L[3:5]

# 跳着取，第三个为步长
print L[:8:2]

# 直接复制
L2 = L[:] # 桶 L2 = L
print L2

# 字符串也支持
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]
