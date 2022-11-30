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


s=input("请输入一组字符串:")
print(f"该字符串逆序为:{s[::-1]}")


print(f'\n')
