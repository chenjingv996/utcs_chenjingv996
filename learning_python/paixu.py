#!/usr/bin/env python
#coding:utf-8
print("*"*60)
num = int(input())
out = []
for i in range(num):
    s = input()
    out.append(s)
out.sort()
for s in out:
    print(s)