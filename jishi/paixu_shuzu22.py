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


while True:
    try:
        n = int(input())
        res = list(map(int, input().split()))
        m = int(input())

        if m == 0:
            print(' '.join(map(str, sorted(res))))
        elif m == 1:
            print(' '.join(map(str, sorted(res)[::-1])))
    
    except:
        break


print(f'\n')
