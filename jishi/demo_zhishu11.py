#!/usr/bin/env python
#coding:utf-8

print("*"*60)

import math

ans=[]
for i in range(2,101):
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        ans.append(i)
print(ans)
print(len(ans))


