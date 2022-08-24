#!/usr/bin/env python
#coding:utf-8

from collections import Counter
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return (Counter(target) == Counter(arr))

