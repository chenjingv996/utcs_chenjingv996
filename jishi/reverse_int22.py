#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time as tm
from datetime import datetime as dt
import sys
import re
import math

print(f"{tm.ctime()}\n")
print(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

class ccc:
    def aaa(self,x:int)->int:
        if x==0:
            return 0
        elif x>0:
            return "".join(list(reversed(str(x))))
        else:
            return "-"+"".join(list(reversed(str(-x))))

bbb=ccc()
print(bbb.aaa(123))
print(bbb.aaa(-234))
print(bbb.aaa(0))


print(f'\n')
