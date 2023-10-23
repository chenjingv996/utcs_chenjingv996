#!/usr/bin/env python
#coding:utf-8

import numpy as np

class ccc:
    def aaa(self,nums:list[int])->int:
        n=len(nums)
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return nums[i]
        return -1
        


bbb=ccc()
print(bbb.aaa([1,2,3,4,1,0,2]))
print(bbb.aaa([1,2,3,0,2]))
print(bbb.aaa([1,2]))
