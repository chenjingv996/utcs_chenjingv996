
#!/usr/bin/python env
#coding:utf-8

import paramiko

host_ip="192.168.3.123"
ad="chenjingv"
pw="123456"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname=host_ip,22,username=ad,password=pd)

stdin, stdout, stderr = ssh.exec_command("pwd")

print stdout.readlines()

ssh.close()
