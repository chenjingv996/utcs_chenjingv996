#!/usr/bin/env python
#coding:utf-8


#paramiko是ansible重要模板之一，支持SSH2远程安全连接，支持认证及密钥方式。可以实现远程命
#令执行、文件传输、中间SSH代理等功能
import paramiko
cmd = "pwd"
task_info = "ps -aux"
# 创建客户端对象
ssh = paramiko.SSHClient()
# 接收并保存新的主机名，此外还有RejectPolicy()拒绝未知的主机名
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# hostname:目标主机地址，port:端口号，username:登录用户名，password:密码
ssh.connect(hostname="192.168.3.123", username="chenjingv", password="123456",
port=22)
# 执行命令，timeout为此次会话的超时时间，返回的是(stdin, stdout, stderr)的三元组
stdin, stdout, stderr = ssh.exec_command(cmd, timeout=20)
# 需要解码才能把返回的内容转换为正常的字符串形式
#print(stdin.read().decode())
print(stdout.read().decode())