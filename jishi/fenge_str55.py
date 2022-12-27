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

a = []
for i in range(2):
    a.append(input())

for word in a:
    while len(word) >= 8:
        print(word[:8])
        word = word[8:]

    if 0 < len(word) < 8:
        print(str(word) + '0' * (8 - len(word)))


print(f'\n')
