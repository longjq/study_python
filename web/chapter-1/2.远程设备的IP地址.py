#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 远程主机名转换为IP
__author__ = 'Administrator'

import socket

def get_remote_machine_info():
    remote_host = 'www.163.com'
    try:
        print "Host Name:%s" % remote_host
        print "IP Address:%s" % socket.gethostbyname(remote_host)
    except socket.error, err_msg:
        print "%s: %s" % (remote_host, err_msg)

if __name__ == '__main__':
    get_remote_machine_info()