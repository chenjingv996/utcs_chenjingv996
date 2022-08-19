#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        s=input()
        l=[0,0,0]
        for i in s:
            l[0]+=int(i.isalpha())
            l[1]+=int(i==' ')
            l[2]+=int(i.isnumeric())
        print(l[0])
        print(l[1])
        print(l[2])
        print(len(s)-l[0]-l[1]-l[2])
    except:
        break
