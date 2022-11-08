#!/usr/bin/env python
#coding:utf-8

import sys

for line in sys.stdin:
    str1=line.split()
    print(len(str1[-1]))

