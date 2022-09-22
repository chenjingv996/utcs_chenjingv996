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

num=float(input())
var=round(num)
if num-var==0.5:
    var=var+1
print(var)

print(f'\n')
