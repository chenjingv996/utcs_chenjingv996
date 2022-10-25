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
    def aaa(self, nums: list[int], target: int) -> list[int]:
        d = {}
        res = []
        for k,v in enumerate(nums):
            if target-v in d:
                res.append([d[target-v],k])
            d[v] = k
        return res




print(ccc().aaa([2,5,8,10],10))
print(ccc().aaa([2,5,7,9,10],12))
print(ccc().aaa([3,3],6))
print(ccc().aaa([2],2))
print(ccc().aaa([3],4))

print(f'\n')
