# -*- coding: utf-8 -*-
__author__ = 'Administrator'

# list
my_list = ['zhoujielun', 'zhangxueyou', 'liudehua']
print my_list
print len(my_list)

# 最后一个元素的索引     len(list) - 1  或者 list[-1]
print my_list[len(my_list) - 1]
print my_list[-1]

# 倒数第二个、第三个
print my_list[-2]
print my_list[-3]

# 末尾追加
my_list.append('Adam') # 返回值是 None
print my_list

# 插入指定位置
my_list.insert(0, 'aaaaaaa') # 返回值是 None
print my_list

# 删除末尾元素
print my_list.pop() # 返回末尾的元素 Adam
print my_list

# 删除指定位置元素
print my_list.pop(0) # 删除aaaa
print my_list

# 多维元素
my_list.insert(len(my_list), ['2w',2,['ddd','ffff']])
print my_list #['zhoujielun', 'zhangxueyou', 'liudehua', ['2w', 2, ['ddd', 'ffff']]]

# 多维元素访问
print my_list[3][2][1] # 返回ffff

# tuple固定的元组，被定义后，每个位置的元素都不能被修改
my_tuple = ('jay', 'bob', 'boom')
print my_tuple

