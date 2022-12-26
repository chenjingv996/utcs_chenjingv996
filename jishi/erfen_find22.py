#!/usr/bin/env python
#coding:utf-8

import time as tm
from datetime import datetime as dt

print("#"*80+"\n")

print(f"\n当前时间为:{tm.ctime()}\n")

class ccc:
    def aaa(self,nums:list[int],target:int)->int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1

bbb=ccc()
print(bbb.aaa([1,2,3,4,5],2))


print(f"\n")
