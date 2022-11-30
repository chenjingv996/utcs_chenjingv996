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



n = int(input("请输入随机数个数:"))
s = sorted(set([int(input()) for i in range(n)]))
for i in s:
        print(i)

        
print(f'\n')
