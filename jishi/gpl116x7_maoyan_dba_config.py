#!/usr/bin/env python
#coding:utf-8

import logging
import telnetlib
import time,os,sys
from datetime import datetime as dt

start_time,end_time=dt.now().ctime(),dt.now().ctime()

class TelnetClient:
    def __init__(self):
        self.host_ip='172.17.100.214'
        self.username='admin'
        self.password='admin123'
        self.cmd_1='en'
        self.cmd_2='terminal page-break disable'
        self.cmd_3='conf t'
        self.tn = telnetlib.Telnet()
          
    def outer(fun_name):
        def wrapper(*args,**kwargs):
            test_exec1="#"*25+"【"+fun_name.__name__+"】"+"脚本测试执行开始!"+"#"*20
            link_tips="设备登录中，请稍后......"
            print(f'\n{test_exec1}\n')
            print(f'\n{link_tips}\n')
            telnetlib.Telnet().logfile=output.write(f'\n{test_exec1}\n\n')
            res=fun_name(*args,**kwargs)
            test_exec2="#"*25+"【"+fun_name.__name__+"】"+"脚本测试执行结束!"+"#"*20
            print(f'\n{test_exec2}\n')
            telnetlib.Telnet().logfile=output.write(f'\n{test_exec2}\n\n')
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
        self.tn.read_until(b'gin: ',timeout=6)
        self.tn.write(self.username.encode('ascii') + b'\n')
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'word: ',timeout=6)
        self.tn.write(self.password.encode('ascii') + b'\n')

        self.tn.read_until(b'> ',timeout=6)
        self.tn.write(self.cmd_1.encode('ascii') + b'\n')

        self.tn.read_until(b'word ',timeout=6)
        self.tn.write(self.password.encode('ascii') + b'\n')

        self.tn.read_until(b'# ',timeout=6)
        self.tn.write(self.cmd_2.encode('ascii') + b'\n')
        
        self.tn.read_until(b'# ',timeout=6)
        self.tn.write(self.cmd_3.encode('ascii') + b'\n')
        # 延时1秒再收取返回结果，给服务端足够响应时间
        time.sleep(1)
        print()
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('utf-8')
        if 'Login incorrect' not in command_result:
            login_res1=self.host_ip+"登录成功!"
            print(f'{login_res1}\n')
            self.tn.logfile=output.write(f'{login_res1}\n')
            return True
        else:
            login_res2=self.host_ip+"登录失败，用户名或密码错误!"
            print(f'{login_res2}\n')
            self.tn.logfile=output.write(f'{login_res2}\n')
            return False

    #退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n\n")

    def pass_res(self,cn):
        res="++"*20+"当前用例"+"【"+cn+"】"+"测试结果为:pass"
        print(f'\n{res}')
        self.tn.logfile=output.write(f'\n{res}\n')
    
    def fail_res(self,cn):
        res="++"*20+"当前用例"+"【"+cn+"】"+"测试结果为:fail"
        print(f'\n{res}')
        self.tn.logfile=output.write(f'\n{res}\n')
    
    def check_res1(self,cn,cmds,check_name,check_words,output_lst):
        for i in range(len(cmds)):
            # 执行命令
            self.tn.write(cmds[i].encode('ascii')+b'\n')
            time.sleep(1)
            # 获取命令结果
            cmds_res = self.tn.read_very_eager().decode('utf-8')
            output_lst.append(cmds_res)
            res="命令"+cmds[i]+"执行结果:"
            print(f'\n{res}\n{cmds_res}\n')
            self.tn.logfile=output.write(f'\n{res}\n{cmds_res}\n')

        print(f'\n{check_name}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n')

        for j in range(len(check_words)):
            if check_words[j] not in output_lst[-1]:
                self.fail_res(cn)
                break
        else:
            self.pass_res(cn)

    def check_res2(self,cn,cmds,check_name,check_words,output_lst):
        for i in range(len(cmds)):
            # 执行命令
            self.tn.write(cmds[i].encode('ascii')+b'\n')
            time.sleep(1)
            # 获取命令结果
            cmds_res = self.tn.read_very_eager().decode('utf-8')
            output_lst.append(cmds_res)
            res="命令"+cmds[i]+"执行结果:"
            print(f'\n{res}\n{cmds_res}\n')
            self.tn.logfile=output.write(f'\n{res}\n{cmds_res}\n')

        print(f'\n{check_name}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n')

        for j in range(len(check_words)):
            if check_words[j] in output_lst[-1]:
                self.fail_res(cn)
                break
        else:
            self.pass_res(cn)

    def check_loop(self,cn,cmds,check_name,check_words,output_lst):
        for i in range(len(cmds)):
            # 执行命令
            self.tn.write(cmds[i].encode('ascii')+b'\n')
            time.sleep(2)
            # 获取命令结果
            cmds_res = self.tn.read_very_eager().decode('utf-8')
            output_lst.append(cmds_res)
            res="命令"+cmds[i]+"执行结果:"
            print(f'\n{res}\n{cmds_res}\n')
            self.tn.logfile=output.write(f'\n{res}\n{cmds_res}\n')

        print(f'\n{check_name}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n')

        for j in range(len(check_words)):
            for k in range(1,11):
                cnt_loop='第'+str(k)+'次检查当前ONU在线状态......'
                print(f'\n{cnt_loop}\n')
                self.tn.logfile=output.write(f'\n{cnt_loop}\n')
                # 执行命令
                self.tn.write(cmds[-1].encode('ascii')+b'\n')
                time.sleep(6)
                # 获取命令结果
                cmds_res = self.tn.read_very_eager().decode('utf-8')
                output_lst.append(cmds_res)
                res_last="命令"+cmds[-1]+"执行结果:"
                print(f'\n{res_last}\n{cmds_res}\n')
                self.tn.logfile=output.write(f'\n{res_last}\n{cmds_res}\n')
            # print(f'\nqwer:{output_lst[-1]}\n')
            if check_words[j] not in output_lst[-1]:
                self.fail_res(cn)
                break
        else:
            self.pass_res(cn)

    @outer
    def check_onu(self):
        self.login_host()

        cn=sys._getframe().f_code.co_name 
        cmds=['show interface gpon-onu creation-information | in 3/3',
              'show interface gpon-onu online-information | in 3/3']
        #检查测试ONU在线状态···
        check_name="tips:检查测试ONU在线状态......"
        check_words=["3/3/1      online"]
        output_lst=[]
        self.check_loop(cn,cmds,check_name,check_words,output_lst)
        
        self.logout_host()    
    
    @outer
    def dba_add_uni(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['no create dba-profile 121-125',
              'show dba-profile all | in chenjingv',
              'create dba-profile 121 name chenjingv121  type1 fix 12240',
              'show dba-profile all | in chenjingv']
        #检查单个dba是否创建成功···
        check_name="tips:检查单个dba是否创建成功......"
        check_words=["121         chenjingv121      type1"]
        output_lst=[]
        self.check_res1(cn,cmds,check_name,check_words,output_lst)
        
        self.logout_host()

    @outer
    def dba_del_uni(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['show dba-profile all | in chenjingv',
              'no create dba-profile 121',
              'show dba-profile all | in chenjingv']
        #检查单个dba是否删除成功···
        check_name='tips:检查单个dba是否删除成功......'
        check_words=["121         chenjingv121      type1"]
        output_lst=[]
        self.check_res2(cn,cmds,check_name,check_words,output_lst)

        self.logout_host()

    @outer
    def dba_add_mul(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['show dba-profile all | in chenjingv',
              'create dba-profile 121 name chenjingv121  type1 fix 12240',
              'create dba-profile 122 name chenjingv122 type2 assure 12480',
              'create dba-profile 123 name chenjingv123 type3 assure 12480 max 51200',
              'create dba-profile 124 name chenjingv124 type4 max 122400',
              'create dba-profile 125 name chenjingv125 type5 fix 12240 assure 12480 max 51200',
              'show dba-profile all | in chenjingv']
        #检查多个dba是否创建成功···
        check_name='tips:检查多个dba是否创建成功......'
        check_words=["121         chenjingv121      type1  12240      0             0",
                     "122         chenjingv122      type2  0          12480         0",
                     "123         chenjingv123      type3  0          12480         51200",
                     "124         chenjingv124      type4  0          0             122400",
                     "125         chenjingv125      type5  12240      12480         51200"]
        output_lst=[] 
        self.check_res1(cn,cmds,check_name,check_words,output_lst)

        self.logout_host()

    @outer
    def dba_del_mul(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['show dba-profile all | in chenjingv',
              'no create dba-profile 121-123',
              'show dba-profile all | in chenjingv']
        #检查多个dba是否删除成功···
        check_name='tips:检查多个dba是否删除成功......'
        check_words=["chenjingv121","chenjingv122","chenjingv123"]
        output_lst=[]
        self.check_res2(cn,cmds,check_name,check_words,output_lst)

        self.logout_host()         

    @outer
    def dba_show(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['show dba-profile all | in chenjingv']
        #检查dba-profile 124和dba-profile 125是否存在···
        check_name='tips:检查dba-profile 124和dba-profile 125是否存在......'
        check_words=["chenjingv124","chenjingv125"]
        output_lst=[]
        self.check_res1(cn,cmds,check_name,check_words,output_lst)

        self.logout_host()

    @outer
    def clear_config(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['no create dba-profile 121-125','show dba-profile all']
        #检查配置dba-profile 121-125是否清除···
        check_name='tips:检查配置dba-profile 121-125是否清除......'
        check_words=['121         chenjingv121',
                     '122         chenjingv122',
                     '123         chenjingv123',
                     '124         chenjingv124',
                     '125         chenjingv125']
        output_lst=[]
        self.check_res2(cn,cmds,check_name,check_words,output_lst)

        self.logout_host()    


if __name__ == '__main__':
    timmer="测试开始时间为:"+str(start_time)
    #打印console时间
    print(f'\n{timmer}\n')
    #创建log文件
    output=open(os.path.join(os.getcwd(),'run_office_console_logfile.log'),'w',encoding='utf-8')
    #打印log时间
    telnetlib.Telnet().logfile=output.write(f'\n{timmer}\n')
    #创建telnet实例
    telnet= TelnetClient()
    # 如果登录结果返加True，则执行命令，然后退出
    telnet.check_onu()
    telnet.dba_add_uni()
    telnet.dba_del_uni()
    telnet.dba_add_mul()
    telnet.dba_del_mul()
    telnet.dba_show()
    telnet.clear_config()
    #将标准输出和标准错误保存到log文件  
    sys.stdout,sys.stderr=output,output

#执行方式：python3 demo_office66_logfile.py