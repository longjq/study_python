# -*- coding: utf-8 -*-
__author__ = 'Administrator'
print '你好啊'

age = 20
if age >= 18:
    print 'your age is',age
    print 'adult'

sum = 0
for x in range(101):
    sum = sum + x

print sum

birth = int( raw_input('birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'