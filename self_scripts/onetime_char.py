#!/usr/bin/env python
#coding:utf-8
print("*"*60)

while True:
    try:
        n=input("请任意输入一组字符串:")
        for i in n:
            if n.count(i)==1:
                print(i)
                break
        else:
            print("-1")
    except:
        break
