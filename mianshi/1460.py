#!/usr/bin/env python
#coding:utf-8



class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return sorted(target) == sorted(arr)

p1=Solution()
r1=p1.canBeEqual([1,2,3,4],[2,3,4,1])
r2=p1.canBeEqual([1,2,3,4],[3,4,1])


print(r1)
print(r2)
print(Solution().canBeEqual([1,2,3,4],[3,4,1,2]))
