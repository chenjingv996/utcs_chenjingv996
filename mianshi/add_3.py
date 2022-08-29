#!/usr/bin/env python
#coding:utf-8

# 注释版
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # 遍历nums中所有元素， 用nums[i]表示
        for i in range(len(nums)):

            # 遍历nums[i]之后的所有元素，用nums[j]表示
            for j in range(len(nums) - i -1):

                # 判断该组合是否满足条件
                if nums[i] + nums[j + i + 1] == target:

                    # 返回满足条件的下标对
                    return [i,j + i + 1]


p1=Solution()
r1=p1.twoSum([1,2,3,4],7)
r2=p1.twoSum([1,2,3,4],4)
r3=p1.twoSum([1,2,3,4],5)
r4=p1.twoSum([1,2,3,4],12)
r5=p1.twoSum([1,2,3,4],5)


print(r1)
print(r2)
print(r3)
print(r4)
print(Solution().twoSum([1,2,3,4],6))

