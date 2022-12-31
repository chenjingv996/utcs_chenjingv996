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
    def aaa(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        res=[]
        # 数组为 null 或者数组长度小于 3，返回 []
        if(not nums) or (n<3):
            return []
        # 对数组进行排序
        nums.sort()
        # 若 nums[0]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回[]
        if(nums[0]>0):
            return []
        # 遍历排序后数组：
        for i in range(n):
            # 对于重复元素：跳过，避免出现重复解
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            # 令左指针 L=i+1，右指针 R=n-1，当 L<R 时，执行循环：
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    # 当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    # 并同时将 L,R 移到下一位置，寻找新的解
                    L=L+1
                    R=R-1
                # 若和大于 0，说明 nums[R] 太大，R 左移
                elif(nums[i]+nums[L]+nums[R]>0):
                    R=R-1
                # 若和小于 0，说明 nums[L] 太小，L 右移
                else:
                    L=L+1
        return res

bbb=ccc()
print(bbb.aaa([-1,0,1,2,-1,4]))

print(f'\n')
