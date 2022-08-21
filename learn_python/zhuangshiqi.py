#!/usr/bin/env python
#coding:utf-8

print("#"*60)

import time
from datetime import datetime 

t1=datetime.now()
t2=datetime.today()

print(t1)
print(t2)
print(t1.strftime("%x"))
print(t1.strftime("%X"))
print(t1.strftime("%c"))
print("\n")
print(f'当前时间为:{t1}')
print(t1.strftime("%Y-%m-%d_%H:%M:%S"))
print(f'当前时间为:{t2.strftime("%Y-%m-%d_%H:%M:%S")}')
print("\n")
