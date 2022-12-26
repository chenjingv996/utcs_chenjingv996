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
        tmp = nums[0]
        max_tmp = tmp
        for i in range(1,len(nums)):
            # 当当前序列加上此时的元素的值大于tmp的值，说明最大序列和可能出现在后续序列中，记录此时的最大值
            if tmp + nums[i]>nums[i]:
                max_tmp = max(max_tmp, tmp+nums[i])
                print(max_tmp)   #debug
                tmp = tmp + nums[i] 
                print(tmp)   #debug
            else:
            #当tmp(当前和)小于下一个元素时，当前最长序列到此为止。以该元素为起点继续找最大子序列,
            # 并记录此时的最大值
                max_tmp = max(max_tmp, tmp, tmp+nums[i], nums[i])
                tmp = nums[i]
        return max_tmp
        

bbb=ccc()
print(bbb.aaa([-2,1,-3,4,-1,2,1,-5,4]))

print(f'\n')
