#!/usr/bin/env python
#coding:utf-8
print("*"*60)
res=[]
for m in range(2,101):
    for i in range(2,m):
        if m%i==0:
            break
    else:
        print(res.append(m))
#print("\n")
