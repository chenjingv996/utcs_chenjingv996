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
    def aaa(self, nums: list[int]) -> int:
        max_f = nums[0]
        pre_f = nums[0]
        for i in range(1, len(nums)):
            pre_f = max(pre_f + nums[i], nums[i])
            max_f = max(pre_f, max_f)
        return max_f

bbb=ccc()
print(bbb.aaa([-2,1,-3,4,-1,2,1,-5,4]))

print(f'\n')
