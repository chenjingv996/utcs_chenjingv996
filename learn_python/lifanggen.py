#!/usr/bin/env python
#coding:utf-8
print("*"*60)
import sys
a=1/3
for n in sys.stdin:
    n=float(n)
    if n>0:
        print("%.1f"%(n**a))
    else:
        print("-"+"%.1f"%(abs(n)**a))
#        print("-"+"%.1f"%((n-2*n)**a))
