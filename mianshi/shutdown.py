#!/usr/bin/env python
#coding:utf-8

import time
from datetime import datetime
import os
import re

print("$"*80+"\n")
print(time.ctime()+"\n")

n=int(input("是否需要关机[1.是 2.否]:"))

while True:

    if n==1:
        os.system("shutdown -s -t 30")
        break
    elif n==2:
        print("已取消关机操作！")
        break
    elif n>2 or n<1:
        print("输入错误！")
        break
    else:
        print("输入异常！")
        break
   
