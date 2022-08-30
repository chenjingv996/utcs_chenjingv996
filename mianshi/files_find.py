#!/usr/bin/env python
#coding:utf-8

print("*"*60)

import glob 
import os
import subprocess

dir1=os.getcwd()
#path=os.system("pwd")

print("当前目录为:%s" %dir1)
print()
#print(f"当前路径为:{path}")
print()

lst1=glob.glob("*.py")
for i in lst1:
    print(i)
print ("\n\n")

lst2=glob.glob("*.sh")
for j in lst2:
    print(j)
print ("\n\n")

total=len(lst1)+len(lst2)

print(f'该目录下共有{total}个文件，其中包含{len(lst1)}个python文件，包含{len(lst2)}个shell文件!')
print ("\n\n")
