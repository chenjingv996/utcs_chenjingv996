#!/usr/bin/env python
#coding:utf-8

import paramiko
import time


hostname = '192.168.10.135'
username = 'admin'
password = 'admin123'


client = paramiko.SSHClient() 			#创建SSH连接
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())	#自动确认陌生设备
client.connect(hostname=hostname,
				username=username,
				password=password) #连接

chan = client.invoke_shell()			#打开channel
chan.send('en \n')		#输入命令
time.sleep(0.5)
chan.send('admin123 \n')		#输入命令
time.sleep(0.5)
chan.send('conf t \n')		#输入命令
time.sleep(0.5)
chan.send('show onu state \n')
time.sleep(0.5)							#设置等待时间
info = chan.recv(99999).decode()		#接收输出信息
client.close()
