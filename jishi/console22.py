#!/usr/bin/env python
#!coding:utf-8

import sys,os  # 需要引入的包

# 以下为包装好的 Logger 类的定义
class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "w", encoding="utf-8")  # 防止编码错误

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

import time  
t = time.strftime("-%Y%m%d-%H%M%S", time.localtime())  # 时间戳
#filename = 'log' + t + '.txt'
filename='aaaa.txt'

log = Logger(filename)  
sys.stdout = log

#print(os.system('arch'))
log.write(os.system("uname -r"))
