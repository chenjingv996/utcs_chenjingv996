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

print(f'{sys.version}\n')

aa=sys.stdin.readline()
bb=input("请输入bb:")
print(len(aa))
print(len(bb))


str1=input("请输入一组字符串:")

print(f'\n其中最后一个字符串长度为:{len(str1.split(" ")[-1])}')

print(f'\n{list(map(lambda x:x**2,range(11)))}')

print(f'\n{list(map(str,range(5)))}')

print(f'\n')
