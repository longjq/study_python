#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

def _private_1(name):
    return 'hello,%s' % name

def _private_2(name):
    return 'hi,%s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# greeting('hello')
