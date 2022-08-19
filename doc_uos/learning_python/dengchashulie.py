#!/usr/bin/env python
#coding:utf-8
print("*"*60)
import sys
for s in sys.stdin:
    try:
        n=int(s)
        d=3
        a1=2
        an=a1+(n-1)*d
        sums=(a1+an)*n/2
        print(int(sums))
    except:
        print(-1)
