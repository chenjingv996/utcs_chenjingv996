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


#n=int(input())
a = []

for i in range(int(input())):
    a.append(int(input()))

for i in sorted(set(a)):
    print(i)

        
print(f'\n')
