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

from math import comb  # 导入库不算代码行（大概

class ccc:
    def aaa(self, rowIndex: int) -> list[int]:
        return [comb(rowIndex, i) for i in range(rowIndex + 1)]

bbb=ccc()
print(bbb.aaa(3))



print(f'\n')
