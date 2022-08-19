#!/usr/bin/env python
#coding:utf-8
print("*"*60)
n=input("请输入一组字符串:")
a=list(n[::-1])
data=list({}.fromkeys(a).keys())
c=int("".join(data))
print(c)
