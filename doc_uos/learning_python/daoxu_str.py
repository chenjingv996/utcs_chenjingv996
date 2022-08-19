#!/usr/bin/env python
#coding:utf-8
print("*"*60)
a=input("请输入字符串:")
b=a.split(' ')
c=list(b)
#print((c[::-1]))
d=c[::-1]
for i in d:
    print (i,end=" ")

