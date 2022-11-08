#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys
import re
import math

class ccc:
    def aaa(self,nums:list[int],target:int)->int:
        length=(len(nums))
        left=0
        right=length-1
        if length<1:
            return -1
        while left<=right:
            mid=int((left+right)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1

print(ccc().aaa([1,2,3,4,5],4))


p1=ccc()
p2=ccc()

print(p1.aaa([1,2,3,4,5],2))
print(p2.aaa([1,2,3,4,5],88))


print(f'\n')
