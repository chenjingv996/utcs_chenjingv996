#!/usr/bin/env python
#coding:utf-8





class ccc:
    def aaa(self, nums: list[int]) -> int:
        # 开始的时候，temp记录第一个数
        temp = nums[0]
        # 第一个数是最大的数
        _max = temp
        # 从index=1的数开始循环
        for i in range(1,len(nums)):
            # 判断 [当前最大值_max、累计最大列表和temp、下一个数] 之中最大的数，并从新赋值给_max
            _max = max(temp+nums[i],nums[i],_max)
            # 如果将下一个数加进事先累积的最大长度列表，发现还更小了，则上次的累积结束，下一个数更大，从新开始累积
            if temp+nums[i] < nums[i]:
                # temp重新开始累积和
                temp = nums[i]
            # 如果累积了下一个数，更大，则继续累积
            else:
                temp = temp+nums[i]


        # 最后返回保存最大和的_max
        return _max


print(ccc().aaa([-2,1,-3,4,-1,2,1,-5,4]))
