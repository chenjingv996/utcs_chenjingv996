#!/usr/bin/env python
#coding:utf-8

import paramiko
import os
import select
import sys
 
# 建立一个socket
trans = paramiko.Transport(('192.168.10.222', 22))
# 启动一个客户端
trans.start_client()
 
# 如果使用rsa密钥登录的话
'''
default_key_file = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')
prikey = paramiko.RSAKey.from_private_key_file(default_key_file)
trans.auth_publickey(username='super', key=prikey)
'''
# 如果使用用户名和密码登录
trans.auth_password(username='chenjingv', password='123456')
# 打开一个通道
channel = trans.open_session()
# 获取终端
channel.get_pty()
# 激活终端，这样就可以登录到终端了，就和我们用类似于xshell登录系统一样
channel.invoke_shell()
# 下面就可以执行你所有的操作，用select实现
# 对输入终端sys.stdin和 通道进行监控,
# 当用户在终端输入命令后，将命令交给channel通道，这个时候sys.stdin就发生变化，select就可以感知
# channel的发送命令、获取结果过程其实就是一个socket的发送和接受信息的过程
while True:
    readlist, writelist, errlist = select.select([channel, sys.stdin,], [], [])
    # 如果是用户输入命令了,sys.stdin发生变化
    if sys.stdin in readlist:
        # 获取输入的内容
        input_cmd = sys.stdin.read(1)
        # 将命令发送给服务器
        channel.sendall(input_cmd)
 
    # 服务器返回了结果,channel通道接受到结果,发生变化 select感知到
    if channel in readlist:
        # 获取结果
        result = channel.recv(1024)
        # 断开连接后退出
        if len(result) == 0:
            print("\r\n**** EOF **** \r\n")
            break
        # 输出到屏幕
        sys.stdout.write(result.decode())
        sys.stdout.flush()
 
# 关闭通道
channel.close()
# 关闭链接
trans.close()
