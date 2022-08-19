#!/usr/bin/env python
#coding:utf-8
print("*"*60)
a=input("请输入字符串:")
b={}
for i in a:
    b[i]=a.count(i)
print(b)
c=a[1:3:1]
print("截取字符串为:"+c)
