#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

class poker(object):

    # 玩家初始化
    def __init__(self, title, boss=False):
        self.__title = title
        self.__boss = boss

    # 发牌
    def card_set(self, card):
        pass

    # 出牌
    def card_send(self):
        pass





    def self_print(self):
        print '%s, %s' % (self.__title, self.__boss)

    def boss_get(self):
        return self.__boss

    def boos_get_str(self):
        if self.__boss :
            return '阿拉地主，侬是个小瘪三~~'
        return '俺是农民'