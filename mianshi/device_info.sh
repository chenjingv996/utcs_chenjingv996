#!/usr/bin/env python
#coding:utf-8


from datetime import datetime
import time
import os

def device_info():
    print()
    print(f'当前时间为:{datetime.now().strftime("%Y_%m_%d %H:%M:%S")}\n')
    time.sleep(1)
    print(f'当前时间为:{time.strftime("%Y-%m-%d %H:%M:%S")}\n')
    time.sleep(1)
    print(f'当前时间为:{time.ctime()}\n')
    print("#"*80)
    print("\n\n")
    print(os.system("uname -a"))
    print(os.system("ip add |grep brd"))
    print(os.system("pwd"))
    print(os.system("fdisk -l |grep sda"))
    print(os.system("lspci -nn | grep -i net"))
    print("\n\n")
   
    


if __name__=="__main__":
    device_info()
