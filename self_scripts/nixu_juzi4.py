#!/usr/bin/env python
#coding:utf-8
print("*"*60)

while True:
    try:
        a=input().strip()
        for i in range(len(a)):
            if not a[i].isalpha():
                a=a.replace(a[i]," ")
        b=a.split(" ")
        b.reverse()
        print(" ".join(b))
    except:
        break

