#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import socket

s = socket.socket()
host = socket.gethostname()
# host = socket.gethostbyname('longjq.com')
# print host
port = 55697

s.connect((host, port))
print s.recv(1024)