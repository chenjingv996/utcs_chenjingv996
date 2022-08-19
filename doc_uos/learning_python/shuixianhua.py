#!/usr/bin/env python
#coding:utf-8
print(60*"*")
for num in range(100,1000):
    c=num%10
    a=num//100
    b=(num-a*100)//10
    if num==c**3+b**3+a**3:
        print("%d是水仙花数"%num)
