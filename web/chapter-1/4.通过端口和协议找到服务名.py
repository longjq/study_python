#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 通过端口和协议找到服务名
__author__ = 'Administrator'

import socket

def find_server_name():
    protocolname = 'tcp'
    for port in [80, 25]:
        print "Port: %s => service name: %s" % (port, socket.getservbyport(port, protocolname))
    print "Port: %s => service name: %s" % (53,socket.getservbyport(53, 'udp'))


if __name__ == '__main__':
    find_server_name()
