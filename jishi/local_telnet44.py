#!/usr/bin/env python
#coding:utf-8

import paramiko
#import threading

ip="192.168.3.123"
ad="chenjingv"
pw="123456"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=ip,port=22,username=ad,password=pw)

cmd="arch;uname -r;df -h;ip add;chenjingv"

stdin, stdout, stderr = ssh.exec_command(cmd)

result=stdout.read()
print (result)

if not result:
    result=stderr.read()
ssh.close()

print(result.decode())
