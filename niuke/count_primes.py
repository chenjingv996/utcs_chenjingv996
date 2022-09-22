#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys
import re
import math

print(f"{time.ctime()}\n")
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

def is_prime(n: int):
    result = True
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            result = False
            break
    return result

def count_primes(n:int)->int:
    count=0
    lst=[]
    for k in range(2,n):
        if is_prime(k):
            count += 1
    return count

print(f'共有素数个数为:{count_primes(10)}')

print()

