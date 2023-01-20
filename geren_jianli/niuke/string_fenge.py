#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys
import re

print(f'{time.ctime()}\n')
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

while True:
    try:
        l = input()
        for i in range(0, len(l), 8):
            print("{0:0<8s}".format(l[i:i+8]))
    except:
        break
        
