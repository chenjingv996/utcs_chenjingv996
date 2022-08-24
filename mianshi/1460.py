#!/usr/bin/env python
#coding:utf-8



class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        a = sorted(target)
        b = sorted(arr)
        if a == b:
            return True
        else:
            return False

p1=Solution()
p1.canBeEqual([1,2,3,4],[2,3,1,4])
