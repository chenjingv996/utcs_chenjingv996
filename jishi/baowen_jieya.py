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

def decompression():
	string = input().strip()
	i,stack,total = 0, [], ""
	while i < len(string):
		if string[i] == "]":
			tmp = ""
			while stack:
				value = stack.pop()
				if value.isalpha():
					tmp += value
				# elif value.isdecimal(): 其实这个也行，判断是不是小数，只是不严谨。
				elif value.isdigit():
					tmp = int(value) * tmp[:: -1]
				else:
					total += tmp
			stack.append(string[i])
			i += 1
			

print(f'\n')
