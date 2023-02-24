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

ipaddr='192.168.3.123'
port=22
username='chenjingv'
pwd='123456'

#cmd=['pwd','uname -r','arch']
cmd='arch'

def excuseRemoteCmd(ipaddr, port, username, pwd, cmd):
    print(ipaddr, port, username, pwd, cmd)
    try:
        # 创建SSH对象
        ssh = paramiko.SSHClient()

        # 允许连接不在know_hosts文件中的主机
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接服务器
        ssh.connect(ipaddr, port=port, username=username,
                    password=pwd, timeout=10)

        # 打开一个Channel并执行命令
        # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
        stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True, timeout=10)
        # 打印执行结果
        # for item in stdout.readlines():
        #     print item
        while not stdout.channel.exit_status_ready():
            result = stdout.readline()
            print(result)
            if stdout.channel.exit_status_ready():
                result = stdout.readlines()
                print(result)
                break
        # 错误打印
        err_list = stderr.readlines()
        if len(err_list) > 0:
            print ('ERROR:' + err_list)
            # exit()

        # 关闭连接
        ssh.close()
        return stdout, stderr
    except Exception as e:
        print(e)
    return stdout, stderr


if __name__=="__main__":
    aaa=excuseRemoteCmd(ipaddr,port,username,pwd,cmd)
    print(aaa)


print(f"\nend_time:{time.ctime()}\n")
    
#https://blog.csdn.net/LanlanDeming/article/details/113700202?spm=1001.2101.3001.6650.4&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-113700202-blog-110885957.pc_relevant_3mothn_strategy_recovery&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-4-113700202-blog-110885957.pc_relevant_3mothn_strategy_recovery&utm_relevant_index=9
#https://www.jb51.net/article/270422.html
#https://blog.51cto.com/u_15079076/4324430

