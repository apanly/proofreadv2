# -*- coding: utf-8 -*-
#!/usr/bin/python
#coding=utf-8
import socket

class Client():
    def __init__(self):
        address = ('127.0.0.1', 10000)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        try:
            s.send("天汽预报\r")
            print s.recv(1024)
        except IOError:
            print 'open err'


c = Client()