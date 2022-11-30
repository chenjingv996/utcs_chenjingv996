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



print(int("".join(map(lambda c:bin(c).replace("0b","").rjust(8,"0"),map(int,input().split(".")))),2))

print(f'\n')
