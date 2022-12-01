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
    def aaa(self,nums:list[int],target)->list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]==target-nums[i]:
                    return [i,j]
        return []


print(ccc().aaa([1,3,5,6],11))
print(ccc().aaa([1,3,5,6],13))

print(f'\n')
