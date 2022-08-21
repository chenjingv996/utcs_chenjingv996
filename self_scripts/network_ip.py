#!/usr/bin/env python
#coding:utf-8
print (60*'*')
print (60*"$")
print (100+200)
import os
os.system("ifconfig | grep -A3 ens")
print(60*'$')
print(os.name)
print(os.getcwd())
print(os.environ.get('PATH'))
print(input("请输入:")[::-1])
print(int(input("请输入16进制数:"),16))
