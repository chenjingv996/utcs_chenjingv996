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
        num=int(input())
        res=[]
        for i in range(num):
            res.append(input())
        for i in sorted(res):
            print(i)
    except:
        break



print(f'\n')
