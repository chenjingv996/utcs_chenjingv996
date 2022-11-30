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



a = input()
c = {}
for i in a:
        c[i] = a.count(i)
for key, value in c.items():
    if value == min(c.values()):
        a = a.replace(key, '')
print(a)

#################################################
print(f'\n')
