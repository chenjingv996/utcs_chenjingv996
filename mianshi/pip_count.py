#!/usr/bin/env python
#coding:utf-8

print("#"*80)

from datetime import datetime
import time
import os
import subprocess

print(datetime.now().strftime("%Y-%m-%d %T")+"\n\n")
time.sleep(2)

curr_time=time.ctime()
print(f'当前时间为:{curr_time}\n\n')

print(os.getcwd()+"\n\n")
