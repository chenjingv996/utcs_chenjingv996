#!/usr/bin/env python
#coding:utf-8

import logging
import telnetlib
import os,sys
from time import sleep
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
        self.uplink_id = sys.argv[2]
        self.onu_type1 ='sfu'
        self.onu_type2 ='hgu'
        self.dba_type1='dba-profile 127'
        self.dba_type2='dba-profile 128'
        self.line_type1='line-profile 127'
        self.line_type2='line-profile 128'
        self.service_type1='service-profile 127'
        self.service_type2='service-profile 128'
        
    def outer(fun_name):
        def wrapper(*args,**kwargs):
            test_exec1="#"*20+"【"+fun_name.__name__+"】"+"脚本测试执行开始!"+"#"*20
            link_tips="设备登录中，请稍后......"
            print(f'\n{test_exec1}\n\n{link_tips}\n')
            telnetlib.Telnet().logfile=output.write(f'\n{test_exec1}\n\n{link_tips}\n')
            res=fun_name(*args,**kwargs)
            test_exec2="#"*20+"【"+fun_name.__name__+"】"+"脚本测试执行结束!"+"#"*20
            print(f'\n{test_exec2}\n')
            telnetlib.Telnet().logfile=output.write(f'\n{test_exec2}\n\n')
            return res
        return wrapper
    
    #此函数实现telnet登录主机
    def login_host(self):
        try:
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
        sleep(1)
        print()
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('utf-8')
        if 'Login incorrect' not in command_result:
            login_res1=self.host_ip+"登录成功!"
            print(f'\n{login_res1}\n')
            self.tn.logfile=output.write(f'\n{login_res1}\n')
            return True
        else:
            login_res2=self.host_ip+"登录失败，用户名或密码错误!"
            print(f'\n{login_res2}\n')
            self.tn.logfile=output.write(f'\n{login_res2}\n')
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
            sleep(2)
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
    
    #指定uplink为ten-gigabitethernet 10/2
    @outer
    def uplink_config(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['vlan 4000',
              'end',
              'show run interface ten-gigabitethernet 10/2',
              'conf t',
              'interface ten-gigabitethernet 10/2',
              'no switchport mode',
              'no switchport trunk native vlan',
              'no switchport trunk allowed vlan',
              'no switchport trunk untagged vlan',
              'switchport mode access',
              'switchport access vlan 4000',
              'end',
              'show run interface ten-gigabitethernet 10/2']
        #配置uplink......
        check_name='tips:配置uplink......'
        check_words=['switchport access vlan 4000']
        output_lst=[]
        print(f'\n{check_name}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n')
        self.check_res1(cn,cmds,check_words,output_lst)
        
        self.logout_host()
    
    #指定uplink为auto接口
    @outer
    def uplink_config_auto(self):
    self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['vlan 4000',
              'end',
              'show run interface ten-gigabitethernet {}'.format(self.uplink_id),
              'conf t',
              'interface ten-gigabitethernet {}'.format(self.uplink_id),
              'no switchport mode',
              'no switchport trunk native vlan',
              'no switchport trunk allowed vlan',
              'no switchport trunk untagged vlan',
              'switchport mode access',
              'switchport access vlan 4000',
              'end',
              'show run interface ten-gigabitethernet {}'.format(self.uplink_id)]
        #配置uplink......
        check_name='tips:配置uplink......'
        check_words=['switchport access vlan 4000']
        output_lst=[]
        print(f'\n{check_name}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n')
        self.check_res1(cn,cmds,check_words,output_lst)
        
        self.logout_host()
    
    #指定downlink为gpon-olt 3/3    
    @outer
    def downlink_config(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['end',
              'show run interface gpon-olt 3/3',
              'conf t',
              'interface gpon-olt 3/3',
              'authorization mode none',
              'no switchport mode',
              'no switchport access vlan',
              'no switchport trunk native vlan',
              'no switchport trunk allowed vlan',
              'no switchport trunk untagged vlan',
              'switchport mode trunk',
              'switchport trunk allowed vlan 4000',
              'yes',
              'end',
              'show run interface gpon-olt 3/3']
        #配置downlink......
        check_name='tips:配置downlink......'
        check_words=['switchport trunk allowed vlan 4000']
        output_lst=[]
        print(f'\n{check_name}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n')
        self.check_res1(cn,cmds,check_words,output_lst)
        
        self.logout_host()
        
    #指定downlink为auto接口
    @outer
    def downlink_config_auto(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['end',
              'show run interface gpon-olt {}'.format(self.pon_id),
              'conf t',
              'interface gpon-olt {}'.format(self.pon_id),
              'authorization mode none',
              'no switchport mode',
              'no switchport access vlan',
              'no switchport trunk native vlan',
              'no switchport trunk allowed vlan',
              'no switchport trunk untagged vlan',
              'switchport mode trunk',
              'switchport trunk allowed vlan 4000',
              'yes',
              'end',
              'show run interface gpon-olt {}'.format(self.pon_id)]
        #配置downlink......
        check_name='tips:配置downlink......'
        check_words=['switchport trunk allowed vlan 4000']
        output_lst=[]
        print(f'\n{check_name}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n')
        self.check_res1(cn,cmds,check_words,output_lst)
        
        self.logout_host()
    
    #检查ONU接口是否存在    
    @outer
    def check_onu_port(self):
        self.login_host()

        cn=sys._getframe().f_code.co_name
        cmds_info='show interface gpon-onu cr'
        #检查测试ONU接口状态......
        check_name='tips:检查测试ONU接口状态......'
        check_words=['{}/{}'.format(self.pon_id,self.onu_id)]
        
        # 执行命令
        self.tn.write(cmds_info.encode('ascii')+b'\n')
        sleep(1)
        # 获取命令结果
        cmds_res_1 = self.tn.read_very_eager().decode('utf-8')
        res_1="命令"+cmds_info+"执行结果:"
        print(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        
        if check_words[0] in cmds_res_1:
            cfg_res_1='该ONU接口{}已存在，程序继续......'.format(check_words[0])
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)
        else:
            cfg_res_2='该ONU接口{}不存在，程序退出......'.format(check_words[0])
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.fail_res(cn)
            sys.exit()           
                
        self.logout_host()    
    
    #配置sfu类型dba模板
    @outer
    def dba_config_sfu(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['create dba-profile 127 name chenjingv127 type4 max 1024000',
              'show {}'.format(self.dba_type1)]
        #配置dba profile···
        check_name='tips:配置{}......'.format(self.dba_type1)
        check_words=['127         chenjingv127      type4']
        output_lst=[]
        
        # 执行命令
        self.tn.write(cmds[-1].encode('ascii')+b'\n')
        sleep(1)
        # 获取命令结果
        cmds_res_1 = self.tn.read_very_eager().decode('utf-8')
        res_1="命令"+cmds[-1]+"执行结果:"
        print(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        
        if check_words[0] in cmds_res_1:
            cfg_res_1='已存在{}类型dba模版-{}，无需重复配置......'.format(self.onu_type1,self.dba_type1)
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)         
        else:
            cfg_res_2='不存在{}类型dba模版-{}，配置中请稍后......'.format(self.onu_type1,self.dba_type1)
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.check_res1(cn,cmds,check_words,output_lst)
        
        self.logout_host()
    
    #配置hgu类型dba模板     
    @outer
    def dba_config_hgu(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['create dba-profile 128 name chenjingv128 type4 max 1024000',
              'show {}'.format(self.dba_type2)]
        #配置dba profile···
        check_name='tips:配置{}......'.format(self.dba_type2)
        check_words=['128         chenjingv128      type4']
        output_lst=[]
        
        # 执行命令
        self.tn.write(cmds[-1].encode('ascii')+b'\n')
        sleep(1)
        # 获取命令结果
        cmds_res_1 = self.tn.read_very_eager().decode('utf-8')
        res_1="命令"+cmds[-1]+"执行结果:"
        print(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        
        if check_words[0] in cmds_res_1:
            cfg_res_1='已存在{}类型dba模版-{}，无需重复配置......'.format(self.onu_type2,self.dba_type2)
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)         
        else:
            cfg_res_2='不存在{}类型dba模版-{}，配置中请稍后......'.format(self.onu_type2,self.dba_type2)
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.check_res1(cn,cmds,check_words,output_lst)
        
        self.logout_host()
    
    #配置sfu类型line模板    
    @outer
    def line_config_sfu(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['gpon-onu-line-profile 127',
              'create tcont 1 dba-profile 127',
              'create gem 1 tcont 1',
              'gem 1 mapping 1 vlan 4000',
              'commit',
              'exit',
              'show gpon-onu-line-profile 127']
        #配置line profile···
        check_name='tips:配置{}......'.format(self.line_type1)
        check_words=['LineProfile Name: profile-127']
        output_lst=[]
        
        # 执行命令
        self.tn.write(cmds[-1].encode('ascii')+b'\n')
        sleep(1)
        # 获取命令结果
        cmds_res_1 = self.tn.read_very_eager().decode('utf-8')
        res_1="命令"+cmds[-1]+"执行结果:"
        print(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        
        if check_words[0] in cmds_res_1:
            cfg_res_1='已存在{}类型line模版-{}，无需重复配置......'.format(self.onu_type1,self.line_type1)
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)         
        else:
            cfg_res_2='不存在{}类型line模版-{}，配置中请稍后......'.format(self.onu_type1,self.line_type1)
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.check_res1(cn,cmds,check_words,output_lst)
        
        self.logout_host()
    
    #配置hgu类型line模板    
    @outer
    def line_config_hgu(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['gpon-onu-line-profile 128',
              'create tcont 1 dba-profile 128',
              'create gem 1 tcont 1',
              'gem 1 mapping 1 vlan 4000',
              'commit',
              'exit',
              'show gpon-onu-line-profile 128']
        #配置line profile···
        check_name='tips:配置{}......'.format(self.line_type2)
        check_words=['LineProfile Name: profile-128']
        output_lst=[]
        
        # 执行命令
        self.tn.write(cmds[-1].encode('ascii')+b'\n')
        sleep(1)
        # 获取命令结果
        cmds_res_1 = self.tn.read_very_eager().decode('utf-8')
        res_1="命令"+cmds[-1]+"执行结果:"
        print(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        
        if check_words[0] in cmds_res_1:
            cfg_res_1='已存在{}类型line模版-{}，无需重复配置......'.format(self.onu_type2,self.line_type2)
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)         
        else:
            cfg_res_2='不存在{}类型line模版-{}，配置中请稍后......'.format(self.onu_type2,self.line_type2)
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.check_res1(cn,cmds,check_words,output_lst)
        
        self.logout_host()

    #配置sfu类型service模板
    @outer
    def service_config_sfu(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['gpon-onu-service-profile 127',
              'port-num ethernet 4',
               'uni ethernet 1-4 vlan mode tagged',
               'uni ethernet 1-4 native vlan 4000',
              'commit',
              'exit',
              'show gpon-onu-service-profile 127 | section-end WLAN']
        #配置service profile···
        check_name='tips:配置{}......'.format(self.service_type1)
        check_words=['ServiceProfile Name: profile-127']
        output_lst=[]
        
        # 执行命令
        self.tn.write(cmds[-1].encode('ascii')+b'\n')
        sleep(1)
        # 获取命令结果
        cmds_res_1 = self.tn.read_very_eager().decode('utf-8')
        res_1="命令"+cmds[-1]+"执行结果:"
        print(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        
        if check_words[0] in cmds_res_1:
            cfg_res_1='已存在{}类型service模版-{}，无需重复配置......'.format(self.onu_type1,self.service_type1)
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)         
        else:
            cfg_res_2='不存在{}类型service模版-{}，配置中请稍后......'.format(self.onu_type1,self.service_type1)
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.check_res1(cn,cmds,check_words,output_lst)
        
        self.logout_host()
    
    #配置hgu类型service模板    
    @outer
    def service_config_hgu(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['gpon-onu-service-profile 128',
              'port-num veip 1',
              'commit',
              'exit',
              'show gpon-onu-service-profile 128 | section-end WLAN']
        #配置service profile···
        check_name='tips:配置{}......'.format(self.service_type2)
        check_words=['ServiceProfile Name: profile-128']
        output_lst=[]
        
        # 执行命令
        self.tn.write(cmds[-1].encode('ascii')+b'\n')
        sleep(1)
        # 获取命令结果
        cmds_res_1 = self.tn.read_very_eager().decode('utf-8')
        res_1="命令"+cmds[-1]+"执行结果:"
        print(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n\n{res_1}\n{cmds_res_1}\n')
        
        if check_words[0] in cmds_res_1:
            cfg_res_1='已存在{}类型service模版-{}，无需重复配置......'.format(self.onu_type2,self.service_type2)
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)         
        else:
            cfg_res_2='不存在{}类型service模版-{}，配置中请稍后......'.format(self.onu_type2,self.service_type2)
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.check_res1(cn,cmds,check_words,output_lst)
        
        self.logout_host()
    
    #绑定对应line及service模板    
    @outer
    def profile_bind(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds_1=['int gpon-onu {}/{}'.format(self.pon_id,self.onu_id),
                'line-profile-id 127',
                '\n\n',
                'service-profile-id 127',
                '\n\n',
                'show interface gpon-onu cr | in {}/{}'.format(self.pon_id,self.onu_id)]
        cmds_2=['int gpon-onu {}/{}'.format(self.pon_id,self.onu_id),
                'line-profile-id 128',
                '\n\n',
                'service-profile-id 128',
                '\n\n',
                'show interface gpon-onu cr | in {}/{}'.format(self.pon_id,self.onu_id)]
        #配置绑定自定义profile···
        check_name='tips:配置绑定自定义profile......'
        check_words_1=['active   127  profile-127      127     profile-127']
        check_words_2=['active   128  profile-128      128     profile-128']
        output_lst=[]
        print(f'\n{check_name}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n')
        
        cmds_type=['show gpon-onu {}/{} capability | in ype'.format(self.pon_id,self.onu_id),
                   'show interface gpon-onu cr | in {}/{}'.format(self.pon_id,self.onu_id)]
        # 执行命令
        self.tn.write(cmds_type[0].encode('ascii')+b'\n')
        sleep(1)
        # 获取命令结果
        cmds_res_0 = self.tn.read_very_eager().decode('utf-8')
        res_0="命令"+cmds_type[0]+"执行结果:"
        print(f'n{res_0}\n{cmds_res_0}\n')
        self.tn.logfile=output.write(f'\n{res_0}\n{cmds_res_0}\n')
        
        # 执行命令
        self.tn.write(cmds_type[-1].encode('ascii')+b'\n')
        sleep(1)
        # 获取命令结果
        cmds_res_1 = self.tn.read_very_eager().decode('utf-8')
        res_1="命令"+cmds_type[-1]+"执行结果:"
        print(f'\n{res_1}\n{cmds_res_1}\n')
        self.tn.logfile=output.write(f'\n{res_1}\n{cmds_res_1}\n')
        
        profile_type1='active   127  profile-127      127     profile-127'
        profile_type2='active   128  profile-128      128     profile-128'
        if self.onu_type1 in cmds_res_0: 
            if profile_type1 in cmds_res_1:
                cfg_res_1='该ONU为{}类型，已绑定自定义模版，无需重复配置......'.format(self.onu_type1)
                print(f'\n{cfg_res_1}\n')
                self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
                self.pass_res(cn)         
            else:
                cfg_res_2='该ONU为{}类型，未绑定自定义模版，配置中请稍后......'.format(self.onu_type1)
                print(f'\n{cfg_res_2}\n')
                self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
                self.check_res1(cn,cmds_1,check_words_1,output_lst)
        else:
            if profile_type2 in cmds_res_1:
                cfg_res_1='该ONU为{}类型，已绑定自定义模版，无需重复配置......'.format(self.onu_type2)
                print(f'\n{cfg_res_1}\n')
                self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
                self.pass_res(cn)         
            else:
                cfg_res_2='该ONU为{}类型，未绑定自定义模版，配置中请稍后......'.format(self.onu_type2)
                print(f'\n{cfg_res_2}\n')
                self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
                self.check_res1(cn,cmds_2,check_words_2,output_lst)
        
        self.logout_host()
    
    #删除所有ONU自定义模板    
    @outer
    def clear_config(self):
        self.login_host()

        cn=sys._getframe().f_code.co_name
        cmds=['show interface gpon-onu creation-information | in {}'.format(self.pon_id),
              'show interface gpon-onu online-information | in {}'.format(self.pon_id),
              'int gpon-olt {}'.format(self.pon_id),
              'no create gpon-onu 1-10',
              '\n\n',
              'exit',
              'no gpon-onu-line-profile 127',
              'show gpon-onu-line-profile 127',
              'no gpon-onu-line-profile 128',
              'show gpon-onu-line-profile 128',
              'no gpon-onu-service-profile 127',
              'show gpon-onu-service-profile 127 | section-end WLAN',
              'no gpon-onu-service-profile 128',
              'show gpon-onu-service-profile 128 | section-end WLAN',
              'no creat dba-profile 127',
              'show dba-profile 127',
              'no creat dba-profile 128',
              'show dba-profile 128',
              'show interface gpon-onu creation-information | in {}'.format(self.pon_id),
              'show interface gpon-onu online-information | in {}'.format(self.pon_id)]
        #删除所有ONU自定义模板···
        check_name='tips:删除所有ONU自定义模板......'
        check_words=['--                   --']
        output_lst=[]
        
        print(f'\n{check_name}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n')
        
        self.check_res1(cn,cmds,check_words,output_lst)
        
        self.logout_host()


if __name__ == '__main__':
    timmer="测试开始时间为:"+str(start_time)
    #打印console时间
    print(f'\n{timmer}\n')
    #创建log文件
    output=open(os.path.join(os.getcwd(),'run_demo_logfile.log'),'w',encoding='utf-8')
    #打印log时间
    telnetlib.Telnet().logfile=output.write(f'\n{timmer}\n')
    #创建telnet实例
    telnet= TelnetClient()
    # 如果登录结果返回True，则执行命令，然后退出
    # telnet.uplink_config()
    telnet.uplink_config_auto()
    # telnet.downlink_config()
    telnet.downlink_config_auto()
    telnet.check_onu_port()
    telnet.dba_config_sfu()
    telnet.dba_config_hgu()
    telnet.line_config_sfu()
    telnet.line_config_hgu()
    telnet.service_config_sfu()
    telnet.service_config_hgu()
    telnet.profile_bind()
    # telnet.clear_config()
    #将标准输出和标准错误保存到log文件  
    sys.stdout,sys.stderr=output,output

#执行方式：python3 demo_xxx.py x/x/x  执行脚本需传递ONU接口为第一个参数
