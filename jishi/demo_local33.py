#!/usr/bin/env python
#coding:utf-8

'''
'''
import logging
import telnetlib
import time
import os,sys
from datetime import datetime as dt

start_time,end_time=dt.now(),dt.now()

output=open(os.path.join(os.getcwd(),'run_local.log'),'w')


print(f'\n测试开始时间为:{start_time}\n')

class TelnetClient:
    def __init__(self):
        self.host_ip='192.168.3.123'
        self.username='chenjingv'
        self.password='123456'
        self.cmd_1='su'
        self.tn = telnetlib.Telnet()
        #self.fn = fn

   # def recode(self):
   #     with open(os.path.join(os.getcwd(),'run_recode.log'),'w') as f:
   #         f.write(str(self.tn.read_all().decode("ascii")))
          
    # 此函数实现telnet登录主机
    #def beg_end(self,fn):
    #    def new_fun(*args,**kwargs):
    #        print("######测试执行开始!######")
    #        abc=fn(*args,**kwargs)
    #        print("######测试执行结束!######")
    #        return abc
    #    return new_fun
    def zhuangsiqi(fun_name):
        def wrapper(*args,**kwargs):
            print(f'\n################{fun_name.__name__}脚本测试执行开始!################\n')
            res=fun_name(*args,**kwargs)
            print(f'\n################{fun_name.__name__}脚本测试执行结束!################\n')
            return res
        return wrapper
    
    def login_host(self):
        try:
            # self.tn = telnetlib.Telnet(host_ip,port=23)
            self.tn.open(self.host_ip,port=23)
        except:
            logging.warning(f'{self.host_ip}网络连接失败!\n')
            return False
        # 等待login出现后输入用户名，最多等待10秒
        self.tn.read_until(b'gin: ',timeout=10)
        self.tn.write(self.username.encode('ascii') + b'\n')
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'word: ',timeout=10)
        self.tn.write(self.password.encode('ascii') + b'\n')

        self.tn.read_until(b'$ ',timeout=10)
        self.tn.write(self.cmd_1.encode('ascii') + b'\n')

        self.tn.read_until(b' ',timeout=10)
        self.tn.write(self.password.encode('ascii') + b'\n')
        
        #self.tn.read_until(b'# ',timeout=10)
        #self.tn.write(cmd_2.encode('ascii') + b'\n')
        # 延时两秒再收取返回结果，给服务端足够响应时间
        time.sleep(2)
        print()
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('ascii')
        if 'Login incorrect' not in command_result:
            logging.warning(f'{self.host_ip}登录成功!\n')
            return True
        else:
            logging.warning(f'{self.host_ip}登录失败，用户名或密码错误!\n')
            return False

    # 此函数实现执行传过来的命令，并输出其执行结果
    #@beg_end
    @zhuangsiqi
    def exec_cmd(self):
        self.login_host()
        cmds=['arch','pwd','uname -r']
        for i in range(len(cmds)):
        # 执行命令
            self.tn.write(cmds[i].encode('ascii')+b'\n')
            time.sleep(1)
        # 获取命令结果
            cmds_res = self.tn.read_very_eager().decode('ascii')
            print(f'\n命令{cmds[i]}执行结果：\n{cmds_res}')
            #res=str(cmds_res)
            self.tn.logfile=output.write(f'{cmds_res}\n')
            #logging.warning(f'命令执行结果：\n{cmds_res}')
        #return res
        print()
        self.logout_host()    
    
    @zhuangsiqi
    def check_ssh(self):
        self.login_host()
        cmds=['ps -ef |grep sshd','netstat -anp | grep :22']
        for i in range(len(cmds)):
            self.tn.write(cmds[i].encode('ascii')+b'\n')
            time.sleep(1)
            cmds_res=self.tn.read_very_eager().decode('ascii')
            print(f'\n命令{cmds[i]}执行结果：\n{cmds_res}')
            self.tn.logfile=output.write(f'{cmds_res}\n')
        print()
        self.logout_host()

    # 退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n\n")

if __name__ == '__main__':
    
    telnet= TelnetClient()
    # 如果登录结果返加True，则执行命令，然后退出
    #if telnet_client.login_host():
    #telnet_client.recode()
    telnet.exec_cmd()
    telnet.check_ssh()
    #    telnet_client.logout_host()
