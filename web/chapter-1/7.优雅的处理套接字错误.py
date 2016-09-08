#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
# ！！！运行失败！！！
'''
C:\Users\Administrator\Desktop\www\study_python\web\chapter-1>python 7.优雅的处理套接字
错误.py --host=127.0.0.1 --port=80 --file=index.html
Traceback (most recent call last):
  File "7.优雅的处理套接字错误.py", line 54, in <module>
    main()
  File "7.优雅的处理套接字错误.py", line 30, in main
    s.connect((host, port))
  File "C:\Python27\lib\socket.py", line 228, in meth
    return getattr(self._sock,name)(*args)
TypeError: an integer is required
'''
import sys
import socket
import argparse

def main():
    parser = argparse.ArgumentParser(description='Socket Error Examples')

    parser.add_argument('--host', action='store', dest='host', required=False)
    parser.add_argument('--port', action='store', dest='port', required=False)
    parser.add_argument('--file', action='store', dest='file', required=False)

    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    # 1.创建socket异常处理
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, e:
        print "Error creating socket: %s " % e
        sys.exit(1)

    # 2.连接主机和端口异常处理
    try:
        s.connect((host, port))
    except socket.gaierror, e:
        print "Address-related error connecting to server: %s " % e
        sys.exit(1)

    # 3.发送数据
    try:
        s.sendall("GET %s HTTP/1.0 \r\n\r\n" % filename)
    except socket.error, e:
        print "Error sending data: %s" % e
        sys.exit(1)

    # 4. 等待返回结果处理
    while 1:
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print "Error receiving data: %s" % e
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf)

if __name__ == '__main__':
    main()