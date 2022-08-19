#!/usr/bin/env python
#coding:utf-8
print("*"*60)
n= input("请输入一组字符串:")
l= []
for i in range(n):
        l.append(input())
        l.sort()
        for i in l:
                print(i)
