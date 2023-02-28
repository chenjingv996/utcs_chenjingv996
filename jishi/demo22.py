#!/usr/bin/env python
#coding:utf-8


#paramiko是ansible重要模板之一，支持SSH2远程安全连接，支持认证及密钥方式。可以实现远程命
#令执行、文件传输、中间SSH代理等功能
import paramiko
import time
from datetime import datetime
import sys
import os


ipaddr = '192.168.3.123'
port = 22
username = 'chenjingv'
pwd = '123456'
cmd = 'pwd && arch && who'

log_file=open(os.path.join(os.getcwd(),'run.log'),'w')
sys.stdout=log_file

def ssh_login(ipaddr, port, username, pwd, cmd):
    try:
        # 创建SSH对象
        ssh = paramiko.SSHClient()

        # 允许连接不在know_hosts文件中的主机
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接服务器
        conn=ssh.connect(ipaddr, port, username, pwd, timeout=10)
        end=sys.stdout.endswith("$")

        if end==True:
            print(end)
            stdin.write("su")
            stdin.write("123456")
        else:
            print("error!")

        
        ssh.close()
        # 打开一个Channel并执行命令
        # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
        #stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True, timeout=60)
    except Exception as e:
        print(e)


if __name__=="__main__":
    print(f'\nstart_time is:{time.ctime()}\n')
    aaa=ssh_login(ipaddr,port,username,pwd,cmd)
    print(aaa)
    print(f'\nend_time is:{time.ctime()}\n')



