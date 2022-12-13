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

s = input()
t = input()
tmp = ''
for i in s:
    for j in range(len(t)):
        if i == t[j]:
            tmp += i
            t = t[j+1:]
            break
if tmp==s:
    print("true") 
else:
    print('false')


print(f'\n')
