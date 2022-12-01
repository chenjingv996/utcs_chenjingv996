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


line_1 = int(input())
line_2 = int(input())
dic = []
for i in range(line_1):
    ss = input().split(' ')
    dic.append(ss)
new_list = sorted(dic,key=lambda x:int(x[1]),reverse=1-line_2)
for i in range(len(new_list)):
    print(*new_list[i])



print(f'\n')
