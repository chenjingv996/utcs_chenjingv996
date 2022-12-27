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

def split_string(string):
    string_list = []
 
    if len(string) <= 8:
        string_list.append(string + '0' * (8 - len(string)))
        return string_list
 
    while len(string) > 8:
        temp = string[0:8]
        string = string[8:]
        string_list.append(temp)
 
    if len(string) > 0:
        string_list.append(string + '0' * (8 - len(string)))
        return string_list
 
#main
s1 = input()
s2 = input()
 
s1_list = split_string(s1)
s2_list = split_string(s2)
 
for element in s1_list:
    print(element)
for element in s2_list:
    print(element)





print(f'\n')
