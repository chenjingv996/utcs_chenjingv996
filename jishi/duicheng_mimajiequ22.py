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



s = input()
num = []
for i in range(len(s)):

    for j in range(i+1,len(s)):
        li = []
        if s[i]==s[j]:
            li = s[i:j+1]
            if s[i:j+1]==li[::-1]:
                num.append(j-i+1)
print(max(num))
#这个应该是针对这道题比较简单的算法，但是效率好像不是很高

print(f'\n')
