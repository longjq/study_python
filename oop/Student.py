#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


aa = Student('longjq', 99)

print aa.get_name()
print aa.get_score()



#aa.hahah = 'hahah我就是hahah'
#print aa.hahah
#aa.print_score()