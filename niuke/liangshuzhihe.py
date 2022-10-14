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


class ccc:
    def aaa(self,nums,target):
        d={}
        n=len(nums)
        for x in range(n):
            if target-nums[x] in d:
                return d[target-nums[x]],x
            else:
                d[nums[x]]=x

print(ccc().aaa([2,5,8,10],10))
print(ccc().aaa([3,3],6))
print(ccc().aaa([2],2))
print(ccc().aaa([3],4))

print(f'\n')
