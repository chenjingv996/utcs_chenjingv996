#!/usr/bin/env python
#coding:utf-8

import time
import sys
import paramiko

class gxl116_maoyan_test:
    # ip = ''
    # cmd_list = []
    def __init__(self, ip, port, user, pwd, cmd_list):
        self.ip = ip
        self.port = port
        self.user = user
        self.pwd = pwd
        self.cmd_list = cmd_list

    def check_onu(self, asy_id=1, verbose=True):
        try:
            print('try shh' + str(asy_id))
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # ssh.connect()
            ssh.connect(ip, port, user, pwd, timeout=5, compress=True)
            print('You have successfully connect to ' + ip + '\n')
        except paramiko.ssh_exception.AuthenticationException:
            print("User authentication failed for " + ip + '.')
        #激活交互式shell
        command = ssh.invoke_shell()
        #等待网络设备回应
        # command.send('system\n')
        #执行具体的命令
        for cmd in cmd_list:
            command.send(cmd)
        time.sleep(2)
        #获取中路由器返回信息
        output = command.recv(65535)
        x = output.decode('ascii')
        #关闭连接
        ssh.close()
        print('SSH 连接关闭！')
        if verbose:
            print(x)
        return x


if __name__ == "__main__":
    #执行命令
    cmd_list = ['admin\n','admin123\n','en\n','admin123\n','$$$auto_test of chenjingv!\n\n','conf t\n\n','show onu state\n\n','end\n\n']
    ip = '192.168.10.135'
    port = 22
    user= 'admin'
    pwd= 'admin123'
    
    sw1 = gxl116_maoyan_test(ip,port,user,pwd,cmd_list)
    sw1.check_onu()
