#!/usr/bin/env python
#coding:utf-8

print(f"{'#'*60}\n")

from datetime import datetime as dt
import time as tm

print(f'{tm.ctime()}\n')

for i in range(1, 10):
    for j in range(1, i+1):
        print('%d*%d=%-3d'%(j, i, i*j), end='\t')
    print()
print()


