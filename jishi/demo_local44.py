#!/usr/bin/env python
#coding:utf-8

import logging
import telnetlib
import time
import os,sys
from datetime import datetime as dt

start_time,end_time=dt.now(),dt.now()


print(f'\n测试开始时间为:{start_time}\n')

class TelnetClient:
    def __init__(self):
        self.host_ip='192.168.3.123'
        self.username='chenjingv'
        self.password='123456'
        self.cmd_1='su'
        self.tn = telnetlib.Telnet()
          
    # 此函数实现telnet登录主机
    def zhuangsiqi(fun_name):
        def wrapper(*args,**kwargs):
            print("\n"+"#"*20+"["+fun_name.__name__+"]"+"脚本测试执行开始!"+"#"*20+"\n")
            res=fun_name(*args,**kwargs)
            print("\n"+"#"*20+"["+fun_name.__name__+"]"+"脚本测试执行结束!"+"#"*20+"\n")
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
        command_result = self.tn.read_very_eager().decode('utf-8')
        if 'Login incorrect' not in command_result:
            print(f'{self.host_ip}登录成功!\n')
            return True
        else:
            print(f'{self.host_ip}登录失败，用户名或密码错误!\n')
            return False
    
    def pass_res(self):
        print("\n"+"--"*20+"当前用例测试结果为:pass"+"\n")

    def fail_res(self):
        print("\n"+"--"*20+"当前用例测试结果为:fail"+"\n")

    @zhuangsiqi
    def exec_cmd(self):
        self.login_host()
        cmds=['arch','pwd','uname -r']
        for i in range(len(cmds)):
        # 执行命令
            self.tn.write(cmds[i].encode('ascii')+b'\n')
            time.sleep(1)
        # 获取命令结果
            cmds_res = self.tn.read_very_eager().decode('utf-8')
            print(f'\n命令{cmds[i]}执行结果：\n{cmds_res}')
            #self.tn.logfile=output.write(f'{cmds_res}\n\n')
            #logging.warning(f'命令执行结果：\n{cmds_res}')
        #return res
        if "gen" in cmds_res[:-1]:
            self.pass_res()
        else:
            self.fail_res()
        self.logout_host()    
    
    @zhuangsiqi
    def check_ssh(self):
        self.login_host()
        cmds=['ip add | grep inet -C2',
              'ps -ef | grep sshd',
              'netstat -anp | grep :22',
              'this is a testing!']
        for i in range(len(cmds)):
            self.tn.write(cmds[i].encode('ascii')+b'\n')
            time.sleep(1)
            cmds_res=self.tn.read_very_eager().decode('utf-8')
            print(f'\n命令{cmds[i]}执行结果：\n{cmds_res}')
            #self.tn.logfile=output.write(f'{cmds_res}\n\n')
        if "gen" in cmds_res[:-1]:
            self.pass_res()
        else:
            self.fail_res()
        self.logout_host()

    # 退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n\n")

if __name__ == '__main__':
    
    #output=open(os.path.join(os.getcwd(),'run_local_console.log'),'w')

    telnet= TelnetClient()
    # 如果登录结果返加True，则执行命令，然后退出
    telnet.exec_cmd()
    telnet.check_ssh()

    #sys.stdout,sys.stderr=output,output
    
