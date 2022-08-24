#!/usr/bin/env python
#coding:utf-8



class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        a = sorted(target)
        b = sorted(arr)
        if a == b:
            return True
        else:
            return False

