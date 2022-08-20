#!/usr/bin/env python
#coding:utf-8
print("*"*60)
a=input("请输入一组字符串:")
lst1=a.split(" ")[::-1]
print(lst1)
print(" ".join(lst1))
