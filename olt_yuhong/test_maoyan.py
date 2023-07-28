#!/usr/bin/env python
#coding:utf-8

import time

print("#"*80+"\n")
print(f"当前时间为:{time.ctime()}\n")

class ccc():
    def aaa(self,nums:list[int],target:int)->list[int]:
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []


bbb=ccc()

print(f'bbb.aaa([1,3,5,6],8)\n')
print(f"测试结果为:{bbb.aaa([1,3,5,6],11)}\n")

print(f'\n')
