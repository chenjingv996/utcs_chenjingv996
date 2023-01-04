#!/usr/bin/env python
#coding:utf-8

# 测试过程中，比较常用的操作就是将DUT(待测物)接入网络中，然后远程操控对DUT，
# 使用SSH远程登陆到主机，然后执行相应的command即可
# python 代码如下：
# paramiko是用python语言写的一个模块，遵循SSH2协议，支持以加密和认证的方式，进行远程服务器的连接
# 首先第一步我们需要安装paramiko这个包
# 安装命令：pip install paramiko
# 导入paramiko包

import paramiko
import telnetlib3

host="192.168.10.253"
ad="admin"
pw="yhkj@123"
ena_pw="yhkj@123"

tn=telnetlib3.Telnet(host)

tn.read_until(b"gin:")
tn.write(ad.encode('ascii')+b'\n')

tn.read_until(b"word:")
tn.write(pw.encode('ascii')+b'\n')

tn.read_until(b">")
tn.write(ena_pw.encode('ascii')+b'\n')

#tn.read_until(b"gin:")
tn.write(b'conf ter\n')






