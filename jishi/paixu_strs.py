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
        stack=[]
        for i in range(num):
            stack.append(input())
        print("\n".join(sorted(stack)))
    except:
        break



print(f'\n')
