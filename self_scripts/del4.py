#!/usr/bin/env python
#coding:utf-8
print("*"*60)
import os
rootdir="/home/chenjingv"
filelist=os.listdir(rootdir)
for f in filelist:
#    print(filelist)
    if ".txt" in f:
        del_file=rootdir+"/"+f
        os.remove(del_file)
        print("删除完成:",del_file)
    if ".txt" not in f:
        print("该类型文件不存在!")
        break
