#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import random
# ==================
import tools

# 数据准备
p1, p2, p3, rest = [], [], [], []
pukes = [
    (103, 3, '3♦'),
    (104, 4, '4♦'),
    (105, 5, '5♦'),
    (106, 6, '6♦'),
    (107, 7, '7♦'),
    (108, 8, '8♦'),
    (109, 9, '9♦'),
    (110, 10, '10♦'),
    (111, 11, 'J♦'),
    (112, 12, 'Q♦'),
    (113, 13, 'K♦'),
    (114, 14, 'A♦'),
    (115, 15, '2♦'),

    (203, 3, '3♣'),
    (204, 4, '4♣'),
    (205, 5, '5♣'),
    (206, 6, '6♣'),
    (207, 7, '7♣'),
    (208, 8, '8♣'),
    (209, 9, '9♣'),
    (210, 10, '10♣'),
    (211, 11, 'J♣'),
    (212, 12, 'Q♣'),
    (213, 13, 'K♣'),
    (214, 14, 'A♣'),
    (215, 15, '2♣'),

    (303, 3,  '3♥'),
    (304, 4,  '4♥'),
    (305, 5,  '5♥'),
    (306, 6,  '6♥'),
    (307, 7,  '7♥'),
    (308, 8,  '8♥'),
    (309, 9,  '9♥'),
    (310, 10, '10♥'),
    (311, 11, 'J♥'),
    (312, 12, 'Q♥'),
    (313, 13, 'K♥'),
    (314, 14, 'A♥'),
    (315, 15, '2♥'),

    (403, 3,  '3♠'),
    (404, 4,  '4♠'),
    (405, 5,  '5♠'),
    (406, 6,  '6♠'),
    (407, 7,  '7♠'),
    (408, 8,  '8♠'),
    (409, 9,  '9♠'),
    (410, 10, '10♥'),
    (411, 11, 'J♥'),
    (412, 12, 'Q♥'),
    (413, 13, 'K♥'),
    (414, 14, 'A♥'),
    (415, 15, '2♥'),

    (501, 99, '小王'),
    (502, 100, '大王')
]

# 洗牌
random.shuffle(pukes)

# 发牌
for index, item in enumerate(pukes):
    if index >= (pukes.__len__() - 3):
        rest.append(item)
    elif index % 3 == 0:
        p1.append(item)
    elif index % 3 == 1:
        p2.append(item)
    elif index % 3 == 2:
        p3.append(item)

# 随机给一个人地主
luck = random.randrange(1, 4)
     # luck = 1
if luck == 1:
        p1.extend(rest)
elif luck == 2:
        p2.extend(rest)
elif luck == 3:
        p3.extend(rest)
else:
    pass


def run():
    if p1.__len__() == 20 :
        print 'P1（地主）：',
        for i in p1:
            print str(i[2])+'('+str(i[1])+')',
    else:
        print 'P1（农民）：地主，快出牌~~~',


    tools.next_line()

    if p2.__len__() == 20 :
        print 'P2（地主）：',
        for i in p2:
            print str(i[2])+'('+str(i[1])+')',
    else:
        print 'P2（农民）：地主，快出牌~~~',

    tools.next_line()

    if p3.__len__() == 20 :
        print 'P3（地主）：',
        for i in p3:
            print str(i[2])+'('+str(i[1])+')',
    else:
        print 'P3（农民）：地主，快出牌~~~',
    # for i in p3:
    #     print str(i[2])+'('+str(i[1])+')',

# 首页启动
if __name__ == '__main__':
    log()
    pass