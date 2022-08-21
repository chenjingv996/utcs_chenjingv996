#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        s = input()
        res = 0
        
        for i in s:
            if i.isupper():
                res+=1
        print(res)
    except:
        break

