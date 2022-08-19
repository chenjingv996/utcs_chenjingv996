#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
        try:
            n=input()
            lst=[]
            for i in range(int(n)):
                lst.append(int(input()))
            uniq=set(lst)
            lst=list(uniq)
            lst.sort()
            for i in lst:
                print(i)
        except:
            break
