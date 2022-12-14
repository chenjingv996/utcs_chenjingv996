#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime as dt
import sys
import re
import math
import let 

print(f"{time.ctime()}\n")
print(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

str1 = input()
str2 = input()
tmp = ''

for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            tmp += str1[i]
            str2=str2[j+1:]
            print(str2)       #debug
            break

if tmp==str1:
    print("true") 
else:
    print('false')


print(f'\n')
