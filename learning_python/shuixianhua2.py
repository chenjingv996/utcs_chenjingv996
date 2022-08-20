#!/usr/bin/env python
#coding:utf-8
print(60*"*")
for a in range(1,10):
    for b in range(0,10):
        for c in range(0,10):
            s1=a*100+b*10+c
            s2=a**3+b**3+c**3
            if s1==s2:
                print("水仙花数有:%d"%s2)
