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


def excuseRemoteCmd(ipaddr, port, username, pwd, cmd):
    print(ipaddr, port, username, pwd, cmd)
    
    log_file=open(os.path.join(os.getcwd(),'log123.txt'),'w')
    sys.stdout=log_file
    
    print(f'\nstart_time:{time.ctime()}\n')

    try:
        # 创建SSH对象
        ssh = paramiko.SSHClient()

        # 允许连接不在know_hosts文件中的主机
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接服务器
        ssh.connect(ipaddr, port, username,
                    pwd, timeout=10)

        # 打开一个Channel并执行命令
        # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
        stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True, timeout=60)
        # 打印执行结果
        # for item in stdout.readlines():
        #     print item
        while not stdout.channel.exit_status_ready():
            result = stdout.readline()
            print(result)
            if stdout.channel.exit_status_ready():
                result = stdout.readlines()
                #print(result)
                for item in result:
                    print(item)
                break
        # 错误打印
        err_list = stderr.readlines()
        if len(err_list) > 0:
            print (f"'ERROR:' + {err_list}")
            # exit()

        # 关闭连接
        ssh.close()
        return stdout, stderr
    except Exception as e:
        print(e)
    return stdout, stderr

    print(f'\nend_time:{time.ctime()}\n')

if __name__=="__main__":
    aaa=excuseRemoteCmd(ipaddr,port,username,pwd,cmd)
    print(aaa)


