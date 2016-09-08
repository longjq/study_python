#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import socket



x = 1
print id(x)

#host = socket.gethostname()
host = raw_input('input host:')
#host = 'www.python.org'
print host
try:
    host_name = socket.gethostbyname(host)
    print "Host name: %s" % host_name
    print "IP address: %s" % socket.gethostbyname(host_name)
except socket.error, err_msg:
    print "%s, %s" %(host, err_msg)