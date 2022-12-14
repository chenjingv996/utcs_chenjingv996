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
    def aaa(self,s:str)->int:
        res=0
        que=[]
        for i in s:
            while i in que:
                que.pop(0)
            que.append(i)
            res=max(res,len(que))
        return res

bbb=ccc()
print(bbb.aaa("qqwerwerrtt"))


print(f'\n')
