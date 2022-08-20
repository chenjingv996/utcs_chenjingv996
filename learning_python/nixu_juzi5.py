#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        str1=list(map(str,input()))
        str1.reverse()
        s="".join(str1)
        print(s)
    except:
        break
