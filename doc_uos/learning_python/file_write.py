#!/usr/bin/env python
#coding:utf-8
print("*"*60)
f = open("demo.txt","w")#打开文件以便写入
print('沧海月明珠有泪',file=f)
print('蓝回日暖玉生烟',file=f)
f.close()