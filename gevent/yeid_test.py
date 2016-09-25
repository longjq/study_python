#!/usr/bin/ env python
# codeing:utf-8
__author__ = 'Administrator'

def simple_generator_func():
    yield 1
    yield 2
    yield 3

gen = simple_generator_func()

for v in gen:
    print v