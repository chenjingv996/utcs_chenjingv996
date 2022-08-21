#!/usr/bin/env python
#coding:utf-8
print("*"*60)
import re
input_val = raw_input()
split_char = re.split(r'\D*', input_val)
print max(split_char, key=len)
