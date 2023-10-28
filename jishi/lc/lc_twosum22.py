#!/usr/bin/env python
#coding:utf-8


class ccc:
    def aaa(self, nums:list[int], target:int)->list[int]:
        dict={}
        for i in range(len(nums)):
            if target-nums[i] in dict:
                print (dict) #debug
                return [dict[target-nums[i]],i]
            dict[nums[i]]=i
            


bbb=ccc()
print(bbb.aaa([2,7,11,15],13))

