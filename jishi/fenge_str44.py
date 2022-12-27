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

s = []
for i in range(2):
    s.append(sys.stdin.readline().strip())

for x in s:
    while len(x) > 8:
        print (x[:8])
        x = x[8:]
    if len(x) <= 8:
        x = x + '0'*(8-len(x))
        print (x) 




print(f'\n')
