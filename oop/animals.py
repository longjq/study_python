#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print 'Dog.....'

class Cat(Animal):
    def run(self):
        print 'Cat.....'




def run_twice(animal):
    animal.run()
    animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

print isinstance(dog, Animal)
print isinstance(dog, Dog)

print isinstance(cat, Animal)
print isinstance(cat, Cat)

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

# print dir(Animal)
print 'ABC'.__len__()