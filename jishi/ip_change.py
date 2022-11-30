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
        print(sum([256 ** j * int(i) for j, i in enumerate(input().split('.')[::-1])]))
        b = int(input())
        print('.'.join([str(b // (256 ** i) % 256) for i in range(3, -1, -1)]))
    except:
        break

print(f'\n')
