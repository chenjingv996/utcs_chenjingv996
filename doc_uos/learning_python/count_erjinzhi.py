#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        n=int(input("请输入一个正整数:"))
        m=bin(n).count("1")
        print("该正整数二进制数为:",bin(n))
        print("该整数二进制数包含1的个数为:",m)
    except:
        break
