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


str = input().split(';')
x, y = 0, 0
for i in str:
    if 2 <= len(i) <= 3:
        if i[0] in ['A', 'D', 'W', 'S'] and i[1:].isdigit():
            if i[0] == 'A':
                x -= int(i[1:])
            if i[0] == 'D':
                x += int(i[1:])
            if i[0] == 'W':
                y += int(i[1:])
            if i[0] == 'S':
                y -= int(i[1:])
print('{0},{1}'.format(x, y))


print(f'\n')
