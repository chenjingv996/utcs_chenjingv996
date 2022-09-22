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

n=int(input())

for i in range(2,int(n/2)+1):
    while n%i==0:
        print(i,end=" ")
        n=n//i
if n==2:
    print(n)

print(f'\n')


