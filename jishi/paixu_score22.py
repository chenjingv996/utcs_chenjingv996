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


n, rank = int(input()), int(input())
s = [input().split() for i in range(n)]
s = sorted(s, key = lambda x : -int(x[1]), reverse=rank)

for i in s:
    print(i[0], i[1])




print(f'\n')
