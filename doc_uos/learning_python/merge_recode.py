#!/usr/bin/env python
#coding:utf-8
print("*"*60)
n=int(input())
dic={}
for i in range(n):
    ab=input().split(" ")
    a,b=int(ab[0]),int(ab[-1])
    dic[a]=dic.get(a,0)+b
dic=sorted(dic.items(),key=lambda x:(x[0]))
for el in dic:
    print(str(el[0])+" "+str(el[1]))
