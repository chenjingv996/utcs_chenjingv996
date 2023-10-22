#!/usr/bin/env python
#coding:utf-8

import numpy as np
from collections import deque

st='abcccd'
dst=deque(st)
print(dst)
p1=dst.pop()
print(dst)
print(p1)
p2=dst.popleft()
print(dst)
print(p2)
print(dst.count('d'))
