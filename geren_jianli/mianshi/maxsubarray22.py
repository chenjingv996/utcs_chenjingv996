#!/usr/bin/env python
#coding:utf-8





class ccc:
    def aaa(self, nums: list[int]) -> int:
        if not nums:
            return 0
        # _max初始化为nums[0]
        _max = nums[0]
        # 从0开始循环，每一个元素都和后面的所有元素累加，找出其中最大值即可
        for i in range(len(nums)):
            _sum = 0
            # 开始累加
            for k in range(i,len(nums)):
                # 每累加一个数，就和_max比较一下，如果更大，则替换_max
                _sum += nums[k]
                _max = _sum if _sum > _max else _max
        
        return _max
        

print(ccc().aaa([-2,1,-3,4,-1,2,1,-5,4]))
