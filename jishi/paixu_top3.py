#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys,re,math

print(f"{time.ctime()}\n")
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')


class ccc:
    def aaa(self,nums:list[int])->str:
        if nums == None or len(nums) < 3:
            print("error!")
            return 
        r1 = r2 = r3 = 0
        i = 0
        while i < len(nums):
            if nums[i] > r1:
                r3 = r2 
                r2 = r1
                r1 = nums[i]
            elif nums[i] > r2 and nums[i] != r1:
                r3 = r2
                r2 = nums[i]
            elif nums[i] > r3 and nums[i] != r2:
                r3 = nums[i]
            i+=1
        return str(f'{r1} {r2} {r3}')


bbb=ccc()


print(bbb.aaa([1,2]))
print(bbb.aaa([13,11,42,22,15,13,23,22,16]))


