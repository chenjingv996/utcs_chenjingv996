#!/usr/bin/env python
#coding:utf-8

import time
import datetime
import paramiko
import telnetlib3
import sys
import re

class monitor:
    def __init__(self,host,ad,pw):
        try:
            client=paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client = client
            print(f"------------开始连接服务器{server_ip}-----------")
            self.client.connect(host, 22, username=ad, password=pw, timeout=4)
            print(f"------------认证成功!.....-----------")
        except:
            print("remote connection failed!")

    def connet_sw(self,cmd):
        try:
            stdin,stdout,stderr=self.client.exec_command(cmd)
            content=stdout.read().decode()
            return content
        except:
            print("link error!")
        finally:
            self.client.close()


print(connect_sw("pwd"))
    
    

#执行方式：./demo.sh 8.200
