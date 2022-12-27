#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime as dt
import sys
import re
import math
from collections import deque

print(f"{time.ctime()}\n")
print(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

class ccc:
    def aaa(self, nums: list[int], k: int) -> list[int]:
        ans = []
        dq = deque()

        for i in range(len(nums)):
            # 只要当前遍历的元素的值比队尾大，让队尾出队列，
            # 最终队列中的最小元素是大于当前元素的
            while dq and dq[-1] < nums[i]:
                dq.pop()
            # 当前遍历的元素入队列， 此时队列中的元素一定是有序的，队列头部最大
            dq.append(nums[i])
            if i >= k - 1:
                # 如果窗口即将失效（下一次循环要失效）的值与当前对列头部的值相同，那么将对头的值出队列，
                # 注意只pop一次，可能两个4，相邻同时是最大值，
                ans.append(dq[0])
                # 从队列中删除即将失效的数据
                if nums[i - k + 1] == dq[0]:
                    dq.popleft()
        return ans

bbb=ccc()
print(bbb.aaa([1,3,-1,-3,5,3,6,7],3))

print(f'\n')
