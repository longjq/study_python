#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import random
import xipai


player1 = {}
player2 = {}
player3 = {}
i = 53

# 生成一家的牌
player1 = xipai.make_puke(xipai.pukes)

for x in player1:
    print x