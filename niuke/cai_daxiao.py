#!/usr/bin/env python
#coding:utf-8

import time
from datetime import datetime
import math
import re
import random

print("#"*80+"\n")
print(f'当前时间为:{time.ctime()}\n')
print(f'当前时间为:{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

num=random.randint(1,101)
print(str(num)+"\n")

while True:
    n=int(input("请输入一个数字:"))
    if n>num:
        print("猜大了!")
    elif n<num:
        print("猜小了!")
    else:
        print("恭喜你猜对了!")
        break

print()
