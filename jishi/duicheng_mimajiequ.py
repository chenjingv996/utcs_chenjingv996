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


password = input()
max_length = 1
for i in range(1, len(password)):
    # 直接以已知最大长度开始
    for j in range((max_length-1) // 2 , len(password[0:i])):
        # 以当前下标字符 的 下一个字符为对称轴，判断两边是否一样
        if password[i - j - 1:i + 1] == password[i + j + 1:i - 1:-1]:
            max_length = len(password[i - j - 1:i + 1]) * 2 - 1
        # 以当前下标字符 和 下一个字符为对称轴
        elif password[i - j - 1:i] == password[i + j:i - 1:-1]:
            max_length = len(password[i - j - 1:i]) * 2
        else:
            # 从最长字符串的长度逐渐递增,不相等则直接跳出
            break
print(max_length)


print(f'\n')
