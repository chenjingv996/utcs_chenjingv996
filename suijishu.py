#!/usr/bin/env python
#coding:utf-8

import random

n=int(input("请输入要查询的个数:"))
data=[]

for i in range(n):
    num=random.randint(0,500)
    data.append(num)
lst1=list(set(data))
lst1.sort()
for j in lst1:
    print(j)
