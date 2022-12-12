#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys
import re
import math

print(f"{time.ctime()}\n")
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

def check(s):
    cu = 0
    cl = 0
    for i in s:
        if i.isupper():
            cu += 1
        elif i.islower():
            cl += 1
    if cu > cl:
        return s.upper()
    elif cu < cl:
        return s.lower()
    else:
        return s

K = int(input())
S = input()
f = S.find('-')
Sf = S[f:].replace("-",'')
l = [S[:f]]
lf = []
for i in range(len(Sf)):
    while Sf:
        lf.append(Sf[:K])
        Sf = Sf[K:]
for s in lf:
    l.append(check(s))
print("-".join(l))

作者：无限
链接：https://leetcode.cn/circle/discuss/niKSMZ/view/mRMgo3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


print(f'\n')
