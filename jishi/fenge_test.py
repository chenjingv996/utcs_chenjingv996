#!/usr/bin/env python
#coding:utf-8

from time import sleep
import telnetlib
import sys

print(sys.argv[1].split('/'))
lst1=sys.argv[1].split('/')
print('/'.join(lst1[:2]))
print(lst1[-1])
