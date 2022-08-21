#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        n=int(input())
        c=0
        for i in range(1,n+1):
            if i%7==0:
                c+=1
            elif "7" in str(i):
                c+=1
        print(c)
    except:
        break

