#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os
path = os.environ.get('PATH')

# print str.split(path,';')
# print os.environ.keys()

# print os.system('dir')

no_notepad = 'C:\\windows\\not_notepad.exe'
os.execl(no_notepad)
notepad = 'C:\\windows\\notepad.exe'
os.execl(notepad)