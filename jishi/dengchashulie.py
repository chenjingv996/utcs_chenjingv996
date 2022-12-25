#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime as dt
import sys
import re
import math

print(f"{time.ctime()}\n")
print(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

n=int(input())
s=[]
for i in range(2,n*3,3):
    s.append(i)

print(sum(s))

print(f'\n')
