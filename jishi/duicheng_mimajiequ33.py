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

def f(s, l, r):
    temp = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        temp = r - l + 1
        l -= 1
        r += 1
    return temp

while True:
    try:
        s = input()
        res = 1
        for i in range(len(s)):
            # 奇数
            res = max(res, f(s, i, i))
            # 偶数
            res = max(res, f(s, i, i + 1))
        print(res)
    except:
        break

print(f'\n')
