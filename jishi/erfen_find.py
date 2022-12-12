#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime as dt
import sys
import re
import math

print(f"{time.ctime()}\n")
print(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')


class ccc():
    def aaa(self,nums:list[int],target:int)->int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            elif target<=nums[mid]:
                r=mid-1
            else:
                l=mid+1
        return -1
bbb=ccc()

print(bbb.aaa([1,2,3,4,5],5))
print(bbb.aaa([1,2,3,4,5],6))
print(bbb.aaa([1,2,3,4,5],2))
print(bbb.aaa([],123))

print(f'\n')
