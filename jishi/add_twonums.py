#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys
import re
import math

class ccc():
    def aaa(self,nums:list[int],target:int)->list[int]:
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []


print(ccc().aaa([1,3,5,6],11))


print(f'\n')
