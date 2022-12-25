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

while True:
    try:
        x1 = int(input())
        if x1 == 1 or x1 == 2:
            print(-1)
        elif (x1+1) % 2 == 0:
            print(2)
        elif x1 % 4 == 0:
            print(3)
        elif (x1-2) % 4 == 0:
            print(4)
    except:
        break


print(f'\n')
