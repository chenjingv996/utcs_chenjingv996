#!/usr/bin/env python
#coding:utf-8
import sys
lst1=[2,3,2,4]
for line in sys.stdin:
    n=int(line.strip())
    if n<3:
        print(-1)
    if n>=3:
        print(lst1[(n-3)%4])


