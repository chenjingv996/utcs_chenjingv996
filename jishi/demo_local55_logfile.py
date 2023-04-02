#!/usr/bin/env python
#coding:utf-8

import logging
import telnetlib
import time,os,sys
from datetime import datetime as dt

start_time,end_time=dt.now(),dt.now()


class TelnetClient:
    def __init__(self):
        self.host_ip='192.168.3.123'
        self.username='chenjingv'
        self.password='123456'
        self.cmd_1='su'
        self.tn = telnetlib.Telnet()
          
    def outer(fun_name):
        def wrapper(*args,**kwargs):
            print("\n"+"#"*20+"["+fun_name.__name__+"]"+"脚本测试执行开始!"+"#"*20+"\n")
            telnetlib.Telnet().logfile=output.write("\n\n"+"#"*20+"["+fun_name.__name__+"]"+
                    "脚本测试执行开始!"+"#"*20+"\n\n")
            res=fun_name(*args,**kwargs)
            print("\n\n"+"#"*20+"["+fun_name.__name__+"]"+"脚本测试执行结束!"+"#"*20+"\n")
            telnetlib.Telnet().logfile=output.write("\n\n"+"#"*20+"["+fun_name.__name__+"]"+
                    "脚本测试执行结束!"+"#"*20+"\n\n")
            return res
        return wrapper
    
    #此函数实现telnet登录主机
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
            #print(f'{self.host_ip}登录成功!\n')
            login_res1=self.host_ip+"登录成功!"
            print(f'{login_res1}\n')
            self.tn.logfile=output.write(f'{login_res1}\n')
            return True
        else:
            #print(f'{self.host_ip}登录失败，用户名或密码错误!\n')
            login_res2=self.host_ip+"登录失败，用户名或密码错误!"
            print(f'{login_res2}\n')
            self.tn.logfile=output.write(f'{login_res2}\n')
            return False
    
    def pass_res(self):
        #print("\n"+"++"*20+"当前用例测试结果为:pass"+"\n")
        res="++"*20+"当前用例测试结果为:pass"
        print(f'\n{res}')
        self.tn.logfile=output.write(f'\n{res}\n')
    
    def fail_res(self):
        #print("\n"+"++"*20+"当前用例测试结果为:fail"+"\n")
        res="++"*20+"当前用例测试结果为:fail"
        print(f'\n{res}')
        self.tn.logfile=output.write(f'\n{res}\n')

    @outer
    def exec_cmd(self):
        self.login_host()
        cmds=['arch','pwd','uname -r']
        for i in range(len(cmds)):
        # 执行命令
            self.tn.write(cmds[i].encode('ascii')+b'\n')
            time.sleep(0.5)
        # 获取命令结果
            cmds_res = self.tn.read_very_eager().decode('utf-8')
            #print(f'\n命令{cmds[i]}执行结果：\n{cmds_res}')
            res="命令"+cmds[i]+"执行结果:"
            print(f'\n{res}\n{cmds_res}\n')
            #self.tn.logfile=output.write(f'{cmds_res}\n\n')
            self.tn.logfile=output.write(f'\n{res}\n{cmds_res}\n')
        if "gen" in cmds_res[:-1]:
            self.pass_res()
        else:
            self.fail_res()
        self.logout_host()    
    
    @outer
    def check_ssh(self):
        self.login_host()
        cmds=['ip add | grep inet -C2',
              'ps -ef | grep sshd',
              'netstat -anp | grep :22',
              'this is a test script!']
        for i in range(len(cmds)):
            self.tn.write(cmds[i].encode('ascii')+b'\n')
            time.sleep(0.5)
            cmds_res=self.tn.read_very_eager().decode('utf-8')
            #print(f'\n命令{cmds[i]}执行结果：\n{cmds_res}')
            res="命令"+cmds[i]+"执行结果:"
            print(f'\n{res}\n{cmds_res}\n')
            #self.tn.logfile=output.write(f'{cmds_res}\n\n')
            self.tn.logfile=output.write(f'\n{res}\n{cmds_res}\n')
        if "gen" in cmds_res[:-1]:
            self.pass_res()
        else:
            self.fail_res()
        self.logout_host()

    #退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n\n")


if __name__ == '__main__':

    timmer="测试开始时间为:"+str(start_time)
    #打印console时间
    print(f'\n{timmer}\n')
    #创建log文件
    output=open(os.path.join(os.getcwd(),'run_local_console_logfile.log'),'w')
    #打印log时间
    telnetlib.Telnet().logfile=output.write(f'\n{timmer}\n')
    #创建telnet实例
    telnet= TelnetClient()
    # 如果登录结果返加True，则执行命令，然后退出
    telnet.exec_cmd()
    telnet.check_ssh()
    #telnet.exec_cmd()
    #telnet.check_ssh()
    #将标准输出和标准错误保存到log文件  
    sys.stdout,sys.stderr=output,output
    
