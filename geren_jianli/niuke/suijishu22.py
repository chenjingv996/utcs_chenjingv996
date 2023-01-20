#!/usr/bin/env python
#coding:utf-8

while True:
    try:
        n=int(input())
        lst1=[]
        for i in range(n):
            lst1.append(int(input()))
        uniq=set(lst1)
        lst2=list(uniq)
        lst2.sort()
        for i in lst2:
            print(i)
    except:
        break


