#!/usr/bin/env python
#coding:utf-8
print("*"*60)
a=input("请输入:").split(" ")
b=list(a)[::1]
for i in b:
    print(i,end=" ")
