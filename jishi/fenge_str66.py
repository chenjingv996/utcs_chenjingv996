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

b=[]

for i in range(2):
    b.append(input())

for w in b:
    while len(w)>=8:
        print(w[:8])
        w=w[8:]

    if 0<len(w)<8:
        print(str(w)+"0"*(8-len(w)))


print(f'\n')
