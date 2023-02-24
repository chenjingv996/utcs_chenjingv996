#!/usr/bin/env python
#coding:utf-8

print("##"*30+"\n")

import time
from datetime import datetime
import sys
import re
import math
import paramiko

print(f"\nstart_time:{time.ctime()}\n")

ip='192.168.3.123'
port=22
ad='chenjingv'
pw='123456'

cmd=['pwd','uname -r','arch']


for i in cmd:
    print(f'{cmd.index(i)+1},{i}')
    print()

mycmd='date && ls -l'

try:
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,ad,pw)
    stdin,stdout,stderr=ssh.exec_command(mycmd,get_pty=True)
    stdin.close()
    while not stdout.channel.exit_status_ready():
        res=stdout.readlines()
        print(f"\n输入命令为:{mycmd}\n")
        print(f"\n输出结果为:{res}\n")
        if "chenjingv"  in str(res):
            print(f"\n测试结果为:PASS\n")
        else:
            print(f"\n测试结果为:FAIL\n")
#            a=stdout.readlines()
#            print(a)
#            break
    ssh.close()

except Exception as e:
    print(e)


print(f"\nend_time:{time.ctime()}\n")

#https://blog.csdn.net/LanlanDeming/article/details/113700202?spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-113700202-blog-110885957.pc_relevant_3mothn_strategy_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-113700202-blog-110885957.pc_relevant_3mothn_strategy_recovery&utm_relevant_index=9
