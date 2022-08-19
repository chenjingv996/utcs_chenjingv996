#!/usr/bin/env python
#coding:utf-8
print("*"*60)
import os
if os.path.exists("a.txt"):
    os.remove("a.txt")
    print("文件删除完毕")
