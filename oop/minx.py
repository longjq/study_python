#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

class Animal(object):
    pass

class Fly(object):
    pass

class Run(object):
    pass

class Dog(Animal, Run):
    pass

class Bird(Animal, FlyMixin):
    pass
