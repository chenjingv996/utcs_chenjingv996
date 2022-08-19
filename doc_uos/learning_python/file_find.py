#!/usr/bin/env python
#coding:utf-8
print("*"*60)
import glob
lst1=glob.glob("*.py")
for i in lst1:
    print(i)
print()
print("该目录总共有%d个python文件"%len(lst1))
