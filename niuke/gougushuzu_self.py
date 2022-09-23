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

max=100
lst=[]

for a in range(2,int(max//math.sqrt(2))+1):
    for b in range(a+1,int(math.sqrt(max**2-a**2))+1,2):
        c=int(math.sqrt(s:=a**2+b**2))
        if c**2==s and math.gcd(a,b)==1:
            lst.append((a,b,c))

for t in lst:
    print(t)

print(f'\ntotal={len(lst)}')

print()



