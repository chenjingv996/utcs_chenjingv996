#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys
import re

print(f"{time.ctime()}\n")
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')


str1=input("请输入一组字符串:")
print(f'其中最后一个字符串长度为:{len(str1.split(" ")[-1])}')

print(f'\n')
