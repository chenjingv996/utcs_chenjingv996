#!/usr/bin/env python
#coding:utf-8
print("*"*60)


a=input()
for i in a:
    if not i.isalpha():
        a=a.replace(i," ")
b=a.split()
print(" ".join(b[::-1]))

