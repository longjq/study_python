#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('echo', help="echo the string your here", type=int)
args = parser.parse_args()
# parser.parse_args()
print args.square**2
