#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 打印出设备名和IPv4地址
__author__ = 'Administrator'

import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print "Host Name:%s" % host_name
    print "IP Address:%s" % ip_address

# 内部执行，将直接执行。外部执行（import）需要手动调用函数print_machine_info()函数执行
if __name__ == '__main__':
    print_machine_info()


