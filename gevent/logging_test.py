#!/usr/bin/ env python
# codeing:utf-8
__author__ = 'Administrator'

import logging

logging.basicConfig(level=logging.DEBUG, format='%(name)s:%(message)s',)

logger = logging.getLevelName('client')

logging.debug('hello world')
