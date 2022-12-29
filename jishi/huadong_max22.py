#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime as dt
import sys
import re
import math
from collections import deque

print(f"{time.ctime()}\n")
print(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

class ccc:
    def aaa(self, nums: list[int], k: int) -> list[int]:
        queue=deque()
        ret=[]
        for i,val in enumerate(nums):
            if len(queue)>0 and queue[0]<i-k:
                queue.popleft()
            while len(queue)>0 and nums[queue[-1]]<val:
                queue.pop()

            queue.append(i)
            if i>=k-1:
                ret.append(nums[queue[0]])
        return ret


bbb=ccc()
print(bbb.aaa([1,3,-1,-3,5,3,6,7],3))

print(f'\n')
