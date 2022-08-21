#!/usr/bin/env python
#coding:utf-8
print("*"*60)
import os
rootdir="/home/chenjingv"
filelist=os.listdir(rootdir)
for f in filelist:
    if ".txt" in f:
        del_file=rootdir+"/"+f
        os.remove(del_file)
        print("删除完成:",del_file)


