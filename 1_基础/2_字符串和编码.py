# -*- coding: utf-8 -*-
__author__ = 'Administrator'

print ord('A')
print '中文哦'

# 格式化地址，%s代表字符串，%d代表整型，%f浮点数，%x十六进制
print 'Hello,%s'%'world'

print 'Hi %s,you have $%d' % ('Michael', 10009)

# 补0
print '===%03d-%02d' % (5, 3)

# 小数位，会出现四舍五入的情况
print '%.3f' % 3.1458

# %s输出,unicode
print 'Hi %s' % '周杰棍的双杰伦'

# 转义输出%
print 'number: %d %%' % 30
