#!/usr/bin/env python
#coding:utf-8

import time
import sys
import paramiko

class TelnetClient():
	"""此代码在Ubuntu18.04以及centos上测试通过,使用windows可能会出现登录返回值不同的问题,有问题的小伙伴自行修改"""
    def __init__(self,):
        self.tn = telnetlib.Telnet()

    # 此函数实现telnet登录主机
    def login_host(self,host_ip,username,password):
        try:
            # self.tn = telnetlib.Telnet(host_ip,port=23)
            self.tn.open(host_ip)
        except:
            print('%s网络连接失败'%host_ip)
            return False
        # 等待login出现后输入用户名，最多等待10秒
        self.tn.read_until(b'login: ',timeout=10)
        self.tn.write(username.encode('ascii') + b'\n')
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'Password: ',timeout=10)
        self.tn.write(password.encode('ascii') + b'\n')
        # 延时两秒再收取返回结果，给服务端足够响应时间
        time.sleep(2)
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('utf-8')
        if 'Login incorrect' not in command_result:
            print('%s登录成功'%host_ip)
            return True
        else:
            print('%s登录失败，用户名或密码错误'%host_ip)
            return False

    # 此函数实现执行传过来的命令，并输出其执行结果
    def execute_some_command(self):
        # 执行命令
        while True:
            command = input("请输入要执行的命令: ")
            if command == "exit":
                break
            self.tn.write(command.encode()+b'\n')
            time.sleep(1)
            # 获取命令结果
            command_result = self.tn.read_very_eager().decode('utf-8')
            print('命令执行结果：%s' % command_result)

    # 退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n")


if __name__ == '__main__':
    host_ip = '要连接的ip'
    username = '用户名'
    password = '密码'
    telnet_client = TelnetClient()
    # 如果登录结果返加True，则执行命令，然后退出
    if telnet_client.login_host(host_ip,username,password):
        telnet_client.execute_some_command()
        telnet_client.logout_host()
