#!/usr/bin/env python
#coding:utf-8

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        N = len(nums)
        for i in range(N):
            rest = target - nums[i]
            if rest in nums:
                j = nums.index(rest) 
                return [i,j]
                break
            else:
                continue

p1=Solution()
r1=p1.twoSum([1,2,3,4],7)
r2=p1.twoSum([1,2,3,4],4)
r3=p1.twoSum([1,2,3,4],12)

print(r1)
print(r2)
print(r3)
