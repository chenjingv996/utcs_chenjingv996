#!/usr/bin/env python
#coding:utf-8
print(60*"#")
nums=[2,3,5,7]
target=10
class Solution:
    def twosum(self,nums,target):
        for i in range(len(nums)):
            if target-num[i] in nums:
                if i!=nums.index(target-num[i]):
                    return i,nums.index(target-num[i])
