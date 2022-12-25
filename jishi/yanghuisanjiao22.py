#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime as dt
import sys
import re
import math

print(f"{time.ctime()}\n")
print(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

class ccc:
    def aaa(self, rowIndex: int) -> list[int]:
        ans=[0]*(rowIndex+1)
        ans[0]=1
        for i in range(rowIndex+1):
            for j in range(i,0,-1):
                ans[j]+=ans[j-1]
        return ans 
# 杨辉三角 可以用排列组合Cnm 或者 倒序循环 当前项等于前一项相加


bbb=ccc()
print(bbb.aaa(3))


print(f'\n')
