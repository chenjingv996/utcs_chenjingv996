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



class ccc():
    def aaa(self,nums:list[int],target:int)->int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            elif target<=nums[mid]:
                r=mid-1
            else target>=nums[mid]:
                l=mid+1
        return -1


print(ccc().aaa([1,2,3,4,5]),5)


print(f'\n')
