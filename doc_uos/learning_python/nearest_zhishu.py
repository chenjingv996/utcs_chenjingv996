#!/usr/bin/env python
#coding:utf-8
print("*"*60)
import math
def isprime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
        else:
            return True
while True:
    try:
        num,start=int(input())
        if num%2==1:
            start=0
        for i in range(start,num,2):
            a,b=num+i,num-i
            if isprime(a) and isprime(b):
                print(b)
                print(a)
                break
    except:
        break
                


