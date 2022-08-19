#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        n=int(input("请输入一个项数n:"))
        res=(2+(3*n-1))*n/2
        print("该数列之和为:",int(res))
    except:
        break
