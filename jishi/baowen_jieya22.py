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

def baowen():
    str1=input.strip()
    i,stack,total=0,[],""
    while i<len(str1):
        if str1[i]=="]":
            tmp=""
            while stack:
                value=stack.pop()
                if value.isalpha():
                    tmp+=value
                elif value.isdigit():
                    tmp=int(value)*tmp[::-1]
            else:
                total+=tmp
        stack.append(str1[i])
        i+=1
    return total

			

print(f'\n')
