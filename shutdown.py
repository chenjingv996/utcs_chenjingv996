#!/usr/bin/env python
#coding:utf-8

import time
from datetime import datetime
import os
import re


print("#"*80+"\n")
print(f"当前时间为:{time.ctime()}\n")
res=input("是否需要关机(是[y/Y]/否[n/N]):")
print()

def get_result():
    if res=="y" or res=="Y":
        os.system("shutdown -s -t 30")
    elif res=="n" or res=="N":
        print("已取消关机操作！")
    else:
        print("输入错误！")


if __name__=="__main__":
    get_result()



