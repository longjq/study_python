#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import socket

s = socket.socket()

host = socket.gethostname()
port = 55697

s.bind((host, port))
s.listen(5)
while True:
    client, addr = s.accept()
    print "Connection...", addr
    client.send('Thank you for connection')
    client.close()

