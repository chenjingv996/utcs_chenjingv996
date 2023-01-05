#!/usr/bin/env python
#coding:utf-8

# 测试过程中，比较常用的操作就是将DUT(待测物)接入网络中，然后远程操控对DUT，
# 使用SSH远程登陆到主机，然后执行相应的command即可
# python 代码如下：
# paramiko是用python语言写的一个模块，遵循SSH2协议，支持以加密和认证的方式，进行远程服务器的连接
# 首先第一步我们需要安装paramiko这个包
# 安装命令：pip install paramiko
# 导入paramiko包

import time
import paramiko

ip = "192.168.3.123"
username = "chenjingv"
password = "admin@123"

#\\创建交换机登陆信息变量
ssh=paramiko.SSHClient()
#\\创建SSH对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#\\允许连接不在know_hosts文件中的主机
ssh.connect(hostname=ip,port=22,username=username,password=password)
#\\SSH方式连接交换机
print("成功连接",ip)

command=ssh.invoke_shell()
#\\调用交换机命令行
command.send("en\n")
command.send("admin@123\n")
command.send("cont ter\n")
#command.send("ip address 192.168.0.124\n")
#command.send("return\n")
#command.send("save\n")
#command.send("y\n")
#\\发送配置命令
time.sleep(1)
#output=command.recv(65535)
#print(output)
#\\设置等待时间并打印回显内容
#ssh.close()
#\\关闭连接


