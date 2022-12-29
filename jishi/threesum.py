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
    def aaa(self,nums:list[int])->list[int]:
        n,ans=len(nums),[]
        nums.sort()
        for i,e in enumerate(nums):
            if i and e == nums[i-1]:
                continue
            l,r,target=i+1,n-1,-e
            while l<r:
                cur=nums[l]+nums[r]
                if cur==target:
                    if not ans or [e,nums[l],nums[r]]!=ans[-1]:
                        ans.append([e,nums[l],nums[r]])
                    l+=1
                    r-=1
                elif cur<target:l+=1
                else:r-=1
        return ans

bbb=ccc()
print(bbb.aaa([-1,0,1,2,-1,4]))

print(f'\n')
