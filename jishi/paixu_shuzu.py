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


x,y,z=input(),input(),input()

print(*sorted(y.split(' '),key=int,reverse=bool(int(z))))



print(f'\n')
