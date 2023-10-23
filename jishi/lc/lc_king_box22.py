#!/usr/bin/env python
#coding:utf-8

import os,sys,time

class ccc:
    def aaa(nums:list[int],k:int)->int:
        for i in range(len(nums)):
            s=','.join(nums[i]).strip()
        return s


bbb=ccc()
print(bbb.aaa([1,2,-1,5,3],3))
