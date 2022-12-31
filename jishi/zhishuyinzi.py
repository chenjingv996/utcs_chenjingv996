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
for i in range (2,int(n**0.5)+1):
    while n%i==0:
        print(i,end=" ")
        n=int(n/i)
#        print(n)   #debug
if n>2:
    print(n)


print(f'\n')
