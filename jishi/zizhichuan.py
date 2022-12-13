#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime as dt
import sys
import re
import math
import let 

print(f"{time.ctime()}\n")
print(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

s = str(input())
t = str(input())

s_len = len(s)
t_len = len(t)
ne = 0
count = 0
for i in range(s_len):
    for j in range(ne,t_len):
        if t[j] == s[i]:

            ne += 1
            count += 1
            break
        else:
            ne += 1

if count == s_len:
    print('true')
else:
    print('false')

print(f'\n')
