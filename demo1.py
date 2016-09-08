# -*- coding: utf-8 -*-

#print u'请问你是？'
#name = raw_input(u'请输入姓名：')
#print u'非常好的名字，%s .欢迎来到范城！' % name.decode('utf-8')


# classmates = [u'中国',u'制造',u'厉害吧'];
# for i in classmates:
#     print i.encode('utf-8')
#
# if not None:
#     print 'if is None'

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print sum

# def log(func):
#     def wrapper(*args, **kw):
#         print ('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print '2015-12-12'
#
# now()

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print "%s %s():" % (text, func.__name__)
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('run now ')
# def now():
#     print '2016-09-07'
#
# # now()
# logrs = log('run now')
# logrs(now)

# import random
#
# print random.randrange(0, 16, 2)

# print 303%100
# print 208%100
# import math
#
# print int(math.floor(308/100))

# print  m , n for m in '♠♥♣♦' for n in [3,4,5,6,7,8,9,10,'J','Q','K','A',2 ]


import random



pukes = [
    (103, 3, '♠'),
    (104, 4, '♠'),
    (105, 5, '♠'),
    (106, 6, '♠'),
    (107, 7, '♠'),
    (108, 8, '♠'),
    (109, 9, '♠'),
    (110, 10, '♠'),
    (111, 'J', '♠'),
    (112, 'Q', '♠'),
    (113, 'K', '♠'),
    (114, 'A', '♠'),
    (115, '2', '♠'),
    (203, 3, '♥'),
    (204, 4, '♥'),
    (205, 5, '♥'),
    (206, 6, '♥'),
    (207, 7, '♥'),
    (208, 8, '♥'),
    (209, 9, '♥'),
    (210, 10, '♥'),
    (211, 'J', '♥'),
    (212, 'Q', '♥'),
    (213, 'K', '♥'),
    (214, 'A', '♥'),
    (215, '2', '♥'),
    (303, 3, '♣'),
    (304, 4, '♣'),
    (305, 5, '♣'),
    (306, 6, '♣'),
    (307, 7, '♣'),
    (308, 8, '♣'),
    (309, 9, '♣'),
    (310, 10, '♣'),
    (311, 'J', '♣'),
    (312, 'Q', '♣'),
    (313, 'K', '♣'),
    (314, 'A', '♣'),
    (315, '2', '♣'),
    (403, 3, '♦'),
    (404, 4, '♦'),
    (405, 5, '♦'),
    (406, 6, '♦'),
    (407, 7, '♦'),
    (408, 8, '♦'),
    (409, 9, '♦'),
    (410, 10, '♦'),
    (411, 'J', '♦'),
    (412, 'Q', '♦'),
    (413, 'K', '♦'),
    (414, 'A', '♦'),
    (415, '2', '♦')
    (501, 'W', '大王'),
    (502, 'w', '小王')
]


# 初始化牌数据
# items = [(str(m), str(n)) for m in ['♠', '♥', '♣', '♦'] for n in [3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', '2']]
# items.append(('⊙', '大王'))
# items.append(('·', '小王'))

# for i in items:
#     print i[0], i[1]

p1, p2, p3, rest = [], [], [], []

# 洗牌
random.shuffle(items)

# 给用户装牌
for index, item in enumerate(items):
    if index >= (items.__len__() - 3):
        rest.append(item)
    elif index % 3 == 0:
        p1.append(item)
    elif index % 3 == 1:
        p2.append(item)
    elif index % 3 == 2:
        p3.append(item)

# 排序

def sort_val(x):
    maps = {'J': 11, 'Q': 12, 'K': 13, 'A': 14, '2': 15, '小王': 16, '大王':17}
    if x[1] in maps:
        return maps.get(x[1])
    return x[1]

sort_items = sorted(p1, cmp, key=sort_val)
for i in p1:
    print i[0], i[1]
print '============================='
for i in sort_items:
    print i[0], i[1]


# 测试打印
def f():
    print 'p1==================='
    for_each(p1)
    print 'p2==================='
    for_each(p2)
    print 'p3==================='
    for_each(p3)
    print '底牌================='
    for_each(rest)

# 工具函数
def for_each(items):
    for x in items:
        print x

# 测试使用
if __name__ == '__main__':
    # f()
    pass