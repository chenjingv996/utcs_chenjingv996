#!/usr/bin/env python
#coding:utf-8



class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return sorted(target) == sorted(arr)

p1=Solution()
r1=p1.canBeEqual()

print(r1([1,2,3,4],[2,3,1,4]))