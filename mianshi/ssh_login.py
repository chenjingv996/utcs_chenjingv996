#!/usr/bin/env python
#coding:utf-8


import paramiko
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在know_hosts文件中的主机
s.connect("192.168.0.123",22,"chenjingv", "123456")
execmd = 'ls' #需要输入的命令
stdin, stdout, stderr = s.exec_command (execmd)
print(stdout.read())
s.close()
























