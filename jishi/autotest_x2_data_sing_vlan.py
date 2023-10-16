#!/usr/bin/env python
#coding:utf-8

import logging
import telnetlib
import os,sys,time
from time import sleep
from datetime import datetime as dt

class TelnetClient:
    def __init__(self):
        self.host_ip='172.17.100.212'
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
        self.dba_type1='dba-profile 115'
        self.dba_type2='dba-profile 116'
        self.line_type1='line-profile 115'
        self.line_type2='line-profile 116'
        self.service_type1='service-profile 115'
        self.service_type2='service-profile 116'
        
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
        # 等待login出现后输入用户名，最多等待1秒
        self.tn.read_until(b'gin: ',timeout=1)
        self.tn.write(self.username.encode('ascii') + b'\r\n')
        # 等待Password出现后输入用户名，最多等待1秒
        self.tn.read_until(b'word: ',timeout=1)
        self.tn.write(self.password.encode('ascii') + b'\r\n')

        self.tn.read_until(b'> ',timeout=1)
        self.tn.write(self.cmd_1.encode('ascii') + b'\r\n')

        self.tn.read_until(b'word ',timeout=1)
        self.tn.write(self.password.encode('ascii') + b'\r\n')

        self.tn.read_until(b'# ',timeout=1)
        self.tn.write(self.cmd_2.encode('ascii') + b'\r\n')
        
        self.tn.read_until(b'# ',timeout=1)
        self.tn.write(self.cmd_3.encode('ascii') + b'\r\n')
        # 延时1秒再收取返回结果，给服务端足够响应时间
        sleep(1)
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('utf-8')
        if 'Login incorrect' not in command_result:
            login_res1=self.host_ip+"登录成功!"
            print(f'{login_res1}\n')
            self.tn.logfile=output.write(f'\n{login_res1}\n')
            return True
        else:
            login_res2=self.host_ip+"登录失败，用户名或密码错误!"
            print(f'{login_res2}\n')
            self.tn.logfile=output.write(f'\n{login_res2}\n')
            return False

    #退出telnet
    def logout_host(self):
        self.tn.read_until(b'# ',timeout=1)
        self.tn.write('end'.encode('ascii') + b'\r\n')
        self.tn.read_until(b'# ',timeout=1)
        self.tn.write(b'exit\r\n')

    def pass_res(self,cn):
        res="++"*20+"当前用例"+"【"+cn+"】"+"测试结果为:pass"
        print(f'\n{res}')
        self.tn.logfile=output.write(f'\n{res}\n')
    
    def fail_res(self,cn):
        res="++"*20+"当前用例"+"【"+cn+"】"+"测试结果为:fail"
        print(f'\n{res}')
        self.tn.logfile=output.write(f'\n{res}\n')
        
    def check_tips(self,check_name):
        print(f'\n{check_name}\n')
        self.tn.logfile=output.write(f'\n{check_name}\n')
    
    def check_res1(self,cn,cmds,check_words,output_lst):        
        for i in range(len(cmds)):
            # 执行命令
            self.tn.write(cmds[i].encode('ascii')+b'\r\n')
            sleep(1)
            # 获取命令结果
            cmds_res = self.tn.read_very_eager().decode('utf-8')
            self.tn.read_until(b'# ',timeout=1)
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
            
    def check_res2(self,cmds,output_lst):        
        for i in range(len(cmds)):
            # 执行命令
            self.tn.write(cmds[i].encode('ascii')+b'\r\n')
            sleep(1)
            # 获取命令结果
            cmds_res = self.tn.read_very_eager().decode('utf-8')
            self.tn.read_until(b'# ',timeout=1)
            output_lst.append(cmds_res)
            res="命令"+cmds[i]+"执行结果:"
            print(f'\n{res}\n{cmds_res}\n')
            self.tn.logfile=output.write(f'\n{res}\n{cmds_res}\n')
            
    
    #检查OLT软件版本是否正确    
    @outer
    def check_olt_version(self):
        self.login_host()
        cn=sys._getframe().f_code.co_name
        cmds=['end','show version']
        #检查测试OLT软件版本状态......
        check_name='tips:检查测试OLT软件版本状态......'
        check_words=['GPL116-X']
        output_lst=[]
       
        self.check_tips(check_name)
        self.check_res2(cmds[-2:],output_lst)
              
        if check_words[0] in output_lst[-1]:
            cfg_res_1='该OLT软件版本已存在，程序继续......'.format(self.uplink_id)
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)
        else:
            cfg_res_2='该OLT软件版本不存在，程序退出......'.format(self.uplink_id)
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.fail_res(cn)
            sys.exit()                          
        self.logout_host()  
    
    #检查ONU软件版本是否正确    
    @outer
    def check_onu_version(self):
        self.login_host()
        cn=sys._getframe().f_code.co_name
        cmds=['show version gpon-onu {}/{} | in sion'.format(self.pon_id,self.onu_id)]
        #检查测试ONU软件版本状态......
        check_name='tips:检查测试ONU软件版本状态......'
        check_words=['active']
        output_lst=[]
       
        self.check_tips(check_name)
        self.check_res2(cmds[-1:],output_lst)
        
        if check_words[0] in output_lst[-1]:
            cfg_res_1='该ONU软件版本已存在，程序继续......'.format(check_words[0])
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)
        else:
            cfg_res_2='该ONU软件版本不存在，程序退出......'.format(check_words[0])
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.fail_res(cn)
            sys.exit()                           
        self.logout_host()
    
    #检查uplink是否存在    
    @outer
    def check_uplink_port(self):
        self.login_host()
        cn=sys._getframe().f_code.co_name
        cmds=['end','show interface ten-gigabitethernet']
        #检查测试uplink状态......
        check_name='tips:检查测试uplink状态......'
        check_words=['ten-gigabitethernet{}'.format(self.uplink_id)]
        output_lst=[]
       
        self.check_tips(check_name)
        self.check_res2(cmds[-2:],output_lst)
        
        if check_words[0] in output_lst[-1]:
            cfg_res_1='该uplink {} 已存在，程序继续......'.format(self.uplink_id)
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)
        else:
            cfg_res_2='该uplink {} 不存在，程序退出......'.format(self.uplink_id)
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.fail_res(cn)
            sys.exit()                           
        self.logout_host()  
        
    #检查downlink是否存在    
    @outer
    def check_downlink_port(self):
        self.login_host()
        cn=sys._getframe().f_code.co_name
        cmds=['show interface gpon-onu cr']
        #检查测试downlink状态......
        check_name='tips:检查测试downlink状态......'
        check_words=['{}/{}'.format(self.pon_id,self.onu_id)]
        output_lst=[]
       
        self.check_tips(check_name)
        self.check_res2(cmds[-1:],output_lst)
        
        if check_words[0] in output_lst[-1]:
            cfg_res_1='该downlink {} 已存在，程序继续......'.format(check_words[0])
            print(f'\n{cfg_res_1}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_1}\n')
            self.pass_res(cn)
        else:
            cfg_res_2='该downlink {} 不存在，程序退出......'.format(check_words[0])
            print(f'\n{cfg_res_2}\n')
            self.tn.logfile=output.write(f'\n{cfg_res_2}\n')
            self.fail_res(cn)
            sys.exit()                           
        self.logout_host()    
       
    #指定uplink为auto接口
    @outer
    def uplink_config_auto(self):
        self.login_host()        
        cn=sys._getframe().f_code.co_name
        cmds=['creat vlan 10,20,30,40,4000,1011-1020 active',
              'end',
              'show run interface ten-gigabitethernet {}'.format(self.uplink_id),
              'conf t',
              'interface ten-gigabitethernet {}'.format(self.uplink_id),
              'no switchport mode',
              'no switchport access vlan',
              'no switchport trunk native vlan',
              'no switchport trunk allowed vlan',
              'no switchport trunk untagged vlan',
              'switchport mode trunk',
              'switchport trunk native vlan 4000',
              'switchport trunk allowed vlan 10,20,30,40,1011-1020,4000 confirm',
              'end',
              'show run interface ten-gigabitethernet {}'.format(self.uplink_id)]
        #配置uplink......
        check_name='tips:配置uplink......'
        check_words=['switchport trunk native vlan 4000']
        output_lst=[]
        
        self.check_tips(check_name)
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
              'mac-address-table station move',
              'authorization mode none',
              'no switchport mode',
              'no switchport access vlan',
              'no switchport trunk native vlan',
              'no switchport trunk allowed vlan',
              'no switchport trunk untagged vlan',
              'switchport mode trunk',
              'switchport trunk allowed vlan 10,20,30,40,1011-1020,4000 confirm',
              'end',
              'show run interface gpon-olt {}'.format(self.pon_id)]
        #配置downlink......
        check_name='tips:配置downlink......'
        check_words=['switchport trunk allowed vlan 10,20,30,40,1011-1020,4000']
        output_lst=[]
        
        self.check_tips(check_name)
        self.check_res1(cn,cmds,check_words,output_lst)        
        self.logout_host()
    
    #配置sfu类型dba模板
    @outer
    def dba_config_sfu(self):
        self.login_host()        
        cn=sys._getframe().f_code.co_name
        cmds=['conf t',
              'create dba-profile 115 name chenjingv115 type4 max 1024000',
              'end',
              'show {}'.format(self.dba_type1)]
        #配置dba profile···
        check_name='tips:配置{}......'.format(self.dba_type1)
        check_words=['115         chenjingv115      type4']
        output_lst=[]
       
        self.check_tips(check_name)
        self.check_res2(cmds[-2:],output_lst)
        
        if check_words[0] in output_lst[-1]:
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
        cmds=['conf t',
              'create dba-profile 116 name chenjingv116 type4 max 1024000',
              'end',
              'show {}'.format(self.dba_type2)]
        #配置dba profile···
        check_name='tips:配置{}......'.format(self.dba_type2)
        check_words=['116         chenjingv116      type4']
        output_lst=[]
       
        self.check_tips(check_name)
        self.check_res2(cmds[-2:],output_lst)
        
        if check_words[0] in output_lst[-1]:
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
        cmds=['conf t',
              'gpon-onu-line-profile 115',
              'create tcont 1 dba-profile 115',
              'mapping-mode vlan',
              # 'create gem 1 tcont 1',
              # 'gem 1 mapping 1 vlan 10',
              # 'create gem 2 tcont 1',
              # 'gem 2 mapping 2 vlan 20',
              # 'create gem 3 tcont 1',
              # 'gem 3 mapping 3 vlan 30',
              # 'create gem 4 tcont 1',
              # 'gem 4 mapping 4 vlan 40',
              'create gem 1 tcont 1',
              'gem 1 mapping 1 vlan 4000',
              # 'gem 1 mapping 1 vlan 1011',
              # 'create gem 2 tcont 1',
              # 'gem 2 mapping 2 vlan 1012',
              # 'create gem 3 tcont 1',
              # 'gem 3 mapping 3 vlan 1013',
              # 'create gem 4 tcont 1',
              # 'gem 4 mapping 4 vlan 1014',
              'commit',
              'exit',
              'end',
              'show gpon-onu-line-profile 115']
        #配置line profile···
        check_name='tips:配置{}......'.format(self.line_type1)
        check_words=['Line Profile Name: profile-115']
        output_lst=[]
       
        self.check_tips(check_name)
        self.check_res2(cmds[-2:],output_lst)
        
        if check_words[0] in output_lst[-1]:
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
        cmds=['conf t',
              'gpon-onu-line-profile 116',
              'create tcont 1 dba-profile 116',
              'mapping-mode vlan',
              # 'create gem 1 tcont 1',
              # 'gem 1 mapping 1 vlan 10',
              # 'create gem 2 tcont 1',
              # 'gem 2 mapping 2 vlan 20',
              # 'create gem 3 tcont 1',
              # 'gem 3 mapping 3 vlan 30',
              # 'create gem 4 tcont 1',
              # 'gem 4 mapping 4 vlan 40',
              'create gem 1 tcont 1',
              'gem 1 mapping 1 vlan 4000',
              # 'gem 1 mapping 1 vlan 1011',
              # 'create gem 2 tcont 1',
              # 'gem 2 mapping 2 vlan 1012',
              # 'create gem 3 tcont 1',
              # 'gem 3 mapping 3 vlan 1013',
              # 'create gem 4 tcont 1',
              # 'gem 4 mapping 4 vlan 1014',
              'commit',
              'exit',
              'end',
              'show gpon-onu-line-profile 116']
        #配置line profile···
        check_name='tips:配置{}......'.format(self.line_type2)
        check_words=['Line Profile Name: profile-116']
        output_lst=[]
       
        self.check_tips(check_name)
        self.check_res2(cmds[-2:],output_lst)
        
        if check_words[0] in output_lst[-1]:
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
        cmds=['conf t',
              'gpon-onu-service-profile 115',
              'port-num ethernet 4',
              'uni ethernet 1-4 vlan mode tagged',
              'uni ethernet 1-4 native vlan 4000',
              # 'uni ethernet 1 native vlan 10',
              # 'uni ethernet 2 native vlan 20',
              # 'uni ethernet 3 native vlan 30',
              # 'uni ethernet 4 native vlan 40',
              # 'uni ethernet 1 native vlan 1011',
              # 'uni ethernet 2 native vlan 1012',
              # 'uni ethernet 3 native vlan 1013',
              # 'uni ethernet 4 native vlan 1014',
              # 'uni ethernet 5 native vlan 1011',
              # 'uni ethernet 6 native vlan 1012',
              # 'uni ethernet 7 native vlan 1013',
              # 'uni ethernet 8 native vlan 1014',
              'commit',
              'exit',
              'end',
              'show gpon-onu-service-profile 115 | include file']
        #配置service profile···
        check_name='tips:配置{}......'.format(self.service_type1)
        check_words=['Service Profile Name: profile-115']
        output_lst=[]
       
        self.check_tips(check_name)
        self.check_res2(cmds[-2:],output_lst)
        
        if check_words[0] in output_lst[-1]:
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
        cmds=['conf t',
              'gpon-onu-service-profile 116',
              'port-num veip 1',
              'commit',
              'exit',
              'end',
              'show gpon-onu-service-profile 116 | include file']
        #配置service profile···
        check_name='tips:配置{}......'.format(self.service_type2)
        check_words=['Service Profile Name: profile-116']
        output_lst=[]
       
        self.check_tips(check_name)
        self.check_res2(cmds[-2:],output_lst)
        
        if check_words[0] in output_lst[-1]:
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
                'line-profile-id 115',
                '\n\n',
                'service-profile-id 115',
                '\n\n',
                'show interface gpon-onu cr | in {}/{}'.format(self.pon_id,self.onu_id)]
        cmds_2=['int gpon-onu {}/{}'.format(self.pon_id,self.onu_id),
                'line-profile-id 116',
                '\n\n',
                'service-profile-id 116',
                '\n\n',
                'show interface gpon-onu cr | in {}/{}'.format(self.pon_id,self.onu_id)]
        #配置绑定自定义profile···
        check_name='tips:配置绑定自定义profile......'
        check_words_1=['active          115     profile-115  115     profile-115']
        check_words_2=['active          116     profile-116  116     profile-116']
        output_lst=[]       
        cmds_type=['show gpon-onu {}/{} capability | in ype'.format(self.pon_id,self.onu_id),
                   'show interface gpon-onu cr | in {}/{}'.format(self.pon_id,self.onu_id)]

        self.check_tips(check_name)
        self.check_res2(cmds_type[-2:],output_lst)
        
        if self.onu_type1 in output_lst[0]: 
            if check_words_1[0] in output_lst[1]:
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
            if check_words_2[0] in output_lst[1]:
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
              'no create gpon-onu {}'.format(self.onu_id),
              '\n\n',
              'exit',
              'no gpon-onu-line-profile 115',
              'end',
              'show gpon-onu-line-profile 115',
              'conf t',
              'no gpon-onu-line-profile 116',
              'end',
              'show gpon-onu-line-profile 116',
              'conf t',
              'no gpon-onu-service-profile 115',
              'end',
              'show gpon-onu-service-profile 115',
              'conf t',
              'no gpon-onu-service-profile 116',
              'end',
              'show gpon-onu-service-profile 116',
              'conf t',
              'no creat dba-profile 115',
              'end',
              'show dba-profile 115',
              'conf t',
              'no creat dba-profile 116',
              'end',
              'show dba-profile 116',
              'show interface gpon-onu creation-information | in {}'.format(self.pon_id),
              'show interface gpon-onu online-information | in {}'.format(self.pon_id)]
        #删除所有ONU自定义模板···
        check_name='tips:删除所有ONU自定义模板......'
        check_words=['--                   --']
        output_lst=[]
       
        self.check_tips(check_name)
        self.check_res1(cn,cmds,check_words,output_lst)        
        self.logout_host()


if __name__ == '__main__':
    start_time,end_time='Test start time is: ','Test end time is: '
    start_cnt=time.perf_counter()
   #创建log文件
    output=open(os.path.join(os.getcwd(),'run_demo_x2_sing_vlan.log'),'w',encoding='utf-8')
    #打印log开始时间
    telnetlib.Telnet().logfile=output.write(f'\n{start_time + dt.now().ctime()}\n')
    #打印console开始时间
    print(f'\n{start_time + dt.now().ctime()}\n')
    #创建telnet实例
    #如果登录结果返回True，则执行命令，然后退出
    telnet= TelnetClient()
    telnet.clear_config()
    # telnet.check_olt_version()
    # telnet.check_onu_version()
    telnet.check_uplink_port()
    telnet.check_downlink_port()
    telnet.uplink_config_auto()
    telnet.downlink_config_auto()    
    telnet.dba_config_sfu()
    telnet.dba_config_hgu()
    telnet.line_config_sfu()
    telnet.line_config_hgu()
    telnet.service_config_sfu()
    telnet.service_config_hgu()
    telnet.profile_bind()
    # telnet.clear_config()
    #打印console结束时间
    print(f'\n{end_time + dt.now().ctime()}\n')
    #打印log结束时间
    telnetlib.Telnet().logfile=output.write(f'\n{end_time + dt.now().ctime()}\n')
    #打印程序耗时
    end_cnt=time.perf_counter()
    elapsed = end_cnt - start_cnt
    print(f'\nTest coast is: {elapsed:.4f}s\n')
    telnetlib.Telnet().logfile=output.write(f'\nTest coast is: {elapsed:.4f}s\n')
    #将标准输出和标准错误保存到log文件  
    sys.stdout,sys.stderr=output,output

#执行方式：python3 demo_xxx.py x/x/x x/x执行脚本需传递2个参数，downlink和uplink
