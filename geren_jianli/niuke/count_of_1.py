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



num=int(input("请输入一个正整数:"))

print(f'\n{bin(num)}')

print(f'\n该正整数在内存中存储时1的个数为:{bin(num).count("1")}')

print(f'\n')
