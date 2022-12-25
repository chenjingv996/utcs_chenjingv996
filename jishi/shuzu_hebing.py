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

n1=int(input())
l1 = [(s) for s in input().split(' ')]
n2=int(input())
l2 = [(s) for s in input().split(' ')]
print(''.join(sorted(list(set(l1+l2)),key=lambda x:int(x))))


print(f'\n')
