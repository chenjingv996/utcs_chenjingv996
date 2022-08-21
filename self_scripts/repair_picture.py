#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        a=input("请输入一组字符串:")
        print("".join(sorted(a)))
    except:
        break
