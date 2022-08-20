#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while 1:
    try:
        n=int(input())
        if input()=="0":
            flag==True
        else:
            flag==False
        ls=[]
        for i in range(n):
            name,score=input().split()
            ls.append((name,int(score)))
            ls.sort(key=lambda x:x[1],reverse=flag)
        for x in ls:
            print(*x)
    except:
        break


