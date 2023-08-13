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
        self.pon_id = '/'.join(sys.argv[1].split('/')[:2])
        self.onu_id = sys.argv[1].split('/')[-1]
        self.onu_mode1 ='SFU'
        self.onu_mode2 ='HGU'
        
    def outer(fun_name):
        def wrapper(*args,**kwargs):
            test_exec1="#"*20+"【"+fun_name.__name__+"】"+"脚本测试执行开始!"+"#"*20
            link_tips="设备登录中，请稍后......"
            print(f'\n{test_exec1}\n')
            print(f'\n{link_tips}\n')
            telnetlib.Telnet().logfile=output.write(f'\n{test_exec1}\n\n')
            telnetlib.Telnet().logfile=output.write(f'\n{link_tips}\n\n')
            res=fun_name(*args,**kwargs)
            test_exec2="#"*20+"【"+fun_name.__name__+"】"+"脚本测试执行结束!"+"#"*20
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
        self.tn.read_until(b'gin: ',timeout=1)
        self.tn.write(self.username.encode('ascii') + b'\n')
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'word: ',timeout=1)
        self.tn.write(self.password.encode('ascii') + b'\n')

        self.tn.read_until(b'> ',timeout=1)
        self.tn.write(self.cmd_1.encode('ascii') + b'\n')

        self.tn.read_until(b'word ',timeout=1)
        self.tn.write(self.password.encode('ascii') + b'\n')

        self.tn.read_until(b'# ',timeout=1)
        self.tn.write(self.cmd_2.encode('ascii') + b'\n')
        
        self.tn.read_until(b'# ',timeout=1)
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
    
    def check_res1(self,cn,cmds,check_words,output_lst):        
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
            time.sleep(3)
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
            time.sleep(6)
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
                time.sleep(3)
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
    def check_onu_intf(self):
        self.login_host()

        cn=sys._getframe().f_code.co_name
        #检查测试ONU接口状态......
        check_name='tips:检查测试ONU接口状态......'
        cmds_1='show interface gpon-onu cr'
        check_words='{}/{}'.format(self.pon_id,self.onu_id)
        # 执行命令
        self.tn.write(cmds_1.encode('ascii')+b'\n')
        time.sleep(1)
        # 获取命令结果
        cmds_res_1 = self.tn.read_very_eager().decode('utf-8')
        res_1="命令"+cmds_1+"执行结果:"
        print(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        
        if check_words in cmds_res_1:
            cfg_res_1='该ONU接口{}已存在，程序继续......'.format(sys.argv[1])
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)
        else:
            cfg_res_2='该ONU接口{}不存在，程序退出......'.format(sys.argv[1])
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.fail_res(cn)
            sys.exit()           
                
        self.logout_host()    
    
    @outer
    def dba_config(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name 
        cmds=['no gpon-onu-line-profile 127',
              'no create dba-profile 127',
              'show dba-profile 127',
              'create dba-profile 127 name chenjingv127 type4 max 1024000',
              'show dba-profile 127']
        #配置dba profile···
        check_name='配置dba profile......'
        check_words=['127         chenjingv127      type4']
        output_lst=[]
        self.check_res1(cn,cmds,check_name,check_words,output_lst)
        
        self.logout_host()

    @outer
    def line_config(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['no gpon-onu-line-profile 127',
              'show gpon-onu-line-profile 127',
              'gpon-onu-line-profile 127',
            #   'mapping-mode port',
              'create tcont 1 dba-profile 127',
              'create gem 1 tcont 1',
              'gem 1 mapping 1 vlan 4000',
              'commit',
              'exit',
              'show gpon-onu-line-profile 127']
        #配置line profile···
        check_name='tips:配置line profile......'
        check_words=['DBA Profile Name: chenjingv127']
        output_lst=[]
        self.check_res1(cn,cmds,check_name,check_words,output_lst)

        self.logout_host()
       
    @outer
    def service_config(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        #检查service profile绑定状态......
        check_name='tips:检查service profile绑定状态......'
        cmds_1='show interface gpon-onu cr | in {}/{}'.format(self.pon_id,self.onu_id)
        cmds=['int gpon-onu {}/{}'.format(self.pon_id,self.onu_id),
              'service-profile-id 1006',
              'show interface gpon-onu cr | in {}/{}'.format(self.pon_id,self.onu_id)]
        #配置service profile···
        check_name='tips:配置service profile......'
        check_words='1006    Def_VEIP'
        output_lst=[]
        # 执行命令
        self.tn.write(cmds_1.encode('ascii')+b'\n')
        time.sleep(1)
        # 获取命令结果
        cmds_res_1 = self.tn.read_very_eager().decode('utf-8')
        res_1="命令"+cmds_1+"执行结果:"
        print(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        
        if check_words in cmds_res_1:
            cfg_res_1='该ONU已绑定默认模版-{}，无需重复配置......'.format(check_words)
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)         
        else:
            cfg_res_2='该ONU未绑定默认模版-{}，配置中请稍后......'.format(check_words)
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.check_res1(cn,cmds,check_words,output_lst)
        
        self.logout_host()

    @outer
    def bind_profile(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['show interface gpon-onu creation-information | in 3/3',
              'show interface gpon-onu online-information | in 3/3',
              'int gpon-onu 3/3/1',
              'state suspend',
              'yes',
              'show interface gpon-onu online-information | in 3/3',
              'show interface gpon-onu creation-information | in 3/3',
              'line-profile-id 127',
              'service-profile-id 127',
              'state active',
              'show interface gpon-onu online-information | in 3/3',
              'show interface gpon-onu creation-information | in 3/3']
        #绑定自定义line profile和service profile···
        check_name='tips:绑定自定义line profile和service profile......'
        check_words=["active   127  profile-127      127     profile-127"]
        output_lst=[]
        self.check_res1(cn,cmds,check_name,check_words,output_lst)

        self.logout_host()         

    @outer
    def clear_config(self):
        self.login_host()

        cn=sys._getframe().f_code.co_name
        cmds=['int gpon-olt 3/3',
              'show interface gpon-onu creation-information | in 3/3',
              'show interface gpon-onu online-information | in 3/3',
              'no create gpon-onu 1',
              'exit',
              'no gpon-onu-line-profile 127',
              'show gpon-onu-line-profile 127',
              'no gpon-onu-service-profile 127',
              'show gpon-onu-service-profile 127',
              'no creat dba-profile 127',
              'show dba-profile 127',
              'show interface gpon-onu online-information | in 3/3',
              'show interface gpon-onu creation-information | in 3/3']
        #将ONU恢复缺省配置···
        check_name='tips:将ONU恢复缺省配置......'
        check_words=['active   1024 Def_P_all']
        output_lst=[]
        self.check_loop(cn,cmds,check_name,check_words,output_lst)
        
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
    telnet.check_onu_intf()
    # telnet.dba_config()
    # telnet.line_config()
    telnet.service_config()
    # telnet.bind_profile()
    # telnet.clear_config()
    #将标准输出和标准错误保存到log文件  
    sys.stdout,sys.stderr=output,output

#执行方式：python3 demo_office66_logfile.py
