#!/usr/bin/env python
#coding:utf-8
print("*"*60)
import os
rootdir="/home/chenjingv"
filelist=os.listdir(rootdir)
flag=False
for f in filelist:
    if ".txt" not in f:
        flag=False
    else:
        flag=True
        del_file=rootdir+"/"+f
        os.remove(del_file)
        print("删除完成:",del_file)
if not flag:
    print("该类型文件不存在!")


