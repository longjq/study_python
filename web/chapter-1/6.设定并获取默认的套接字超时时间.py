#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import socket

def test_socket_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 返回None，禁用了socket操作的超时时间
    print "Default socket timeout: %s" % s.gettimeout()
    s.settimeout(100)
    print "Current socket timeout: %s"% s.gettimeout()

if __name__ == '__main__':
    test_socket_timeout()