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



x = int(input())
dic = {}
for i in range(x):
    a = input()
    k = int(a.split(' ')[0])
    v = int(a.split(' ')[1])
    if k in dic.keys():
        dic[k] = dic[k]+v
    else:
        dic[k] = v

for key, value in sorted(dic.items()):
    print(key, value)


print(f'\n')
