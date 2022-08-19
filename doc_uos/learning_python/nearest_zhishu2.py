#!/usr/bin/env python
#coding:utf-8
print("*"*60)
import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        num ,start= int(input()) // 2,1
        if num%2==1:
            start=0
        for i in range(start, num, 2):
            a, b = num + i, num - i
            if isPrime(a) and isPrime(b):
                print(b)
                print(a)
                break

    except:
        break
