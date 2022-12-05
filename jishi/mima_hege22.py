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


while True:
    try:
        s = input()
        if len(s) <= 8:
            print('NG')
        else:
            l = [0, 0, 0, 0]
            for i in s:
                if 'a' <= i <= 'z':
                    l[0] = 1
                elif 'A' <= i <= 'Z':
                    l[1] = 1
                elif i.isdigit():
                    l[2] = 1
                else:
                    l[3] = 1
            if sum(l) < 3:
                print('NG')
            else:
                for i in range(len(s)-2):
                    x = s[i:i+3]
                    if x in s[i+3:]:
                        print('NG')
                        break
                else:
                    print('OK')      
    except:
        break



print(f'\n')
