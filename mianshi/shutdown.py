#!/usr/bin/env python
#coding:utf-8


print("$"*80)

import time
from datetime import datetime
import os
import re

n=int(input("是否需要关机(1.是 2.否):"))

while True:
    try:
        if n==1:
            os.system("shutdown -s -t 30")
        elif n==2:
            print("已取消关机操作！")
            break
        else:
            print("输入错误！")
            break
    except:
        break
   

