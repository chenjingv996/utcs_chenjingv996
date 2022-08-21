#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        num=int(input())
        stack=[]
        for i in range(num):
            stack.append(input())
        print("\n".join(sorted(stack)))
    except:
        break
