#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        n=int(input())
        l=[]
        for i in range(1,n):
            p=0
            for y in range(1,i):
                if i%y==0:
                    p+=y
            if i==p:
                l.append(p)
        print(len(l))
    except:
        break
            

