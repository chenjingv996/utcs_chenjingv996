#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        n=input()
        a=set()
        for _ in range(n):
            a.add(int(input()))
        for i in sorted(list(a)):
            print(i)
    except:
        break
