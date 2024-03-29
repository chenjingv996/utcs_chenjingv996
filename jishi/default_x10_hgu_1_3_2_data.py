#!/usr/bin/env python
#coding:utf-8

import logging
import telnetlib
import time,os,sys
from datetime import datetime as dt

start_time,end_time=dt.now().ctime(),dt.now().ctime()

class TelnetClient:
    def __init__(self):
        self.host_ip='172.17.100.216'
        self.username='admin'
        self.password='admin'
        self.cmd_1='en'
        self.cmd_2='no pause'
        self.cmd_3='configure'
        self.tn = telnetlib.Telnet()
          
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
        self.tn.read_until(b'gin: ',timeout=6)
        self.tn.write(self.username.encode('ascii') + b'\n')
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'word: ',timeout=6)
        self.tn.write(self.password.encode('ascii') + b'\n')
        # 禁用翻页
        self.tn.read_until(b'# ',timeout=6)
        self.tn.write(self.cmd_2.encode('ascii') + b'\n')
        # 进入配置模式
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
        #res="++"*20+"当前用例测试结果为:pass"
        res="++"*20+"当前用例"+"【"+cn+"】"+"测试结果为:pass"
        print(f'\n{res}')
        self.tn.logfile=output.write(f'\n{res}\n')
    
    def fail_res(self,cn):
        #res="++"*20+"当前用例测试结果为:fail"
        res="++"*20+"当前用例"+"【"+cn+"】"+"测试结果为:fail"
        print(f'\n{res}')
        self.tn.logfile=output.write(f'\n{res}\n')
    
    def check_res1(self,cn,cmds,check_name,check_words,output_lst):
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
    def check_onu(self):
        self.login_host()

        cn=sys._getframe().f_code.co_name
        cmds=['exit',
              'slot 1 interface gpon-olt 1/3',
              'brief-show slot 1 interface gpon-olt 1/3  ont 2',
              'auto-register',
              'no ont 2',
              'brief-show slot 1 interface gpon-olt 1/3  ont 2',
              'brief-show slot 1 ont-info 3 detail']
        #检查测试ONU在线状态···
        check_name='tips:检查测试ONU在线状态......'
        check_words=['1/3/2    ready']
        output_lst=[]
        self.check_loop(cn,cmds,check_name,check_words,output_lst)
        
        self.logout_host()    
    
    @outer
    def uplink_config(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name 
        cmds=['l2',
              'vlan',
              'brief-show vlan interface xge 3',
              'no interface xge 3 vid 4000',
              'brief-show vlan interface xge 3',
              'interface xge 3 vid 4000 untag',
              'show 4000']
        #配置上联口,指定上联口为xge 3···
        check_name='tips:配置上联口,指定上联口为xge 3···'
        check_words=['vlan untag port',
                     'XGE 3']
        output_lst=[]
        self.check_res1(cn,cmds,check_name,check_words,output_lst)
        
        self.logout_host()

    @outer
    def downlink_config(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name 
        cmds=['brief-show slot 1 interface gpon-olt 1/3']
        #配置下联口,指定下联口为gpon-olt 1/3···
        check_name='tips:配置下联口,指定下联口为gpon-olt 1/3···'
        check_words=['auto-register']
        output_lst=[]
        self.check_res1(cn,cmds,check_name,check_words,output_lst)
        
        self.logout_host()

    @outer
    def profile_dba(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name 
        cmds=['exit',
              'slot 1 interface gpon-olt 1/3',
              'ont 2',
              'no service',
              'home',
              'slot 1',
              'no gpon profile tcont-bind 128 1',
              'no gpon profile tcont-svc 128',
              'no gpon profile dba 128',
              'brief-show slot 1 gpon profile dba 128',
              'gpon profile dba id 128 type4 max 1024000',
              'brief-show slot 1 gpon profile dba 128']
        #配置dba profile......
        check_name='配置dba profile......'
        check_words=['128 newprof_dba_128  type4']
        output_lst=[]
        self.check_res1(cn,cmds,check_name,check_words,output_lst)
        
        self.logout_host()

    @outer
    def profile_flow(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['exit',
              'slot 1 interface gpon-olt 1/3',
              'ont 2',
              'no service',
              'home',
              'slot 1',
              'no gpon profile flow 128 1',
              'brief-show slot 1 gpon profile flow 128',
              'gpon profile flow id 128 1 uni-type veip uni-bitmap 0xf upmap-type vlanId 4000 4000 pri-bitmap 0xff vport 1',
              'brief-show slot 1 gpon profile flow 128']
        #配置profile_flow......
        check_name='tips:配置profile_flow......'
        check_words=['profile id1           :128',
                     'profile name          :newprofile_128',
                     'uni type              :veip']
        output_lst=[]
        self.check_res1(cn,cmds,check_name,check_words,output_lst)

        self.logout_host()

    @outer
    def profile_tcont_svc(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['exit',
              'slot 1 interface gpon-olt 1/3',
              'ont 2',
              'no service',
              'home',
              'slot 1',
              'no gpon profile tcont-bind 128 1',
              'no gpon profile tcont-svc 128',
              'brief-show slot 1 gpon profile tcont-svc 128',
              'gpon profile tcont-svc id 128  dba-id 128',
              'brief-show slot 1 gpon profile tcont-svc 128']
        #配置profile_tcont_svc......
        check_name='tips:配置profile_tcont_svc......'
        check_words=['128 newprofile_128']
        output_lst=[] 
        self.check_res1(cn,cmds,check_name,check_words,output_lst)

        self.logout_host()

    @outer
    def profile_tcont_bind(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['exit',
              'slot 1 interface gpon-olt 1/3',
              'ont 2',
              'no service',
              'home',
              'slot 1',
              'no gpon profile tcont-bind 128 1',
              'brief-show slot 1 gpon profile tcont-bind 128',
              'gpon profile tcont-bind id 128 v-port 1  vportsvc-id 1 tcont-id 1 tcontsvc-id 128',
              'brief-show slot 1 gpon profile tcont-bind 128']
        #配置profile_tcont_bind......
        check_name='tips:配置profile_tcont_bind......'
        check_words=["128 1      newprofile_128"]
        output_lst=[]
        self.check_res1(cn,cmds,check_name,check_words,output_lst)

        self.logout_host()      
        
    @outer
    def svc_type(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['exit',
              'slot 1 interface gpon-olt 1/3',
              'ont 2',
              'no service',
              'virtual-port 1 encrypt disable',
              'service flow-profile 128 tcont-bind-profile 128',
              'brief-show slot 1 interface gpon-olt 1/3 ont 2']
        #配置onu绑定svc_type......
        check_name='tips:配置onu绑定svc_type......'
        check_words=["service flow-profile 128 tcont-bind-profile 128 svc-type 1_"]
        output_lst=[]
        self.check_res1(cn,cmds,check_name,check_words,output_lst)

        self.logout_host()     

    @outer
    def port_vlan(self):
        self.login_host()
        
        cn=sys._getframe().f_code.co_name
        cmds=['exit',
              'slot 1 interface gpon-olt 1/3',
              'ont 1',
              'brief-show slot 1 interface gpon-olt 1/3  ont 1',
              'no port-vlan 1 1',
            #   'no port-vlan 1',
              'no port-vlan 2 1',
            #   'no port-vlan 2',
              'no port-vlan 3 1',
            #   'no port-vlan 3',
              'no port-vlan 4 1',
            #   'no port-vlan 4',
              'brief-show slot 1 interface gpon-olt 1/3  ont 1',
              'port-vlan 1 downstream inverse-upstream intpid 0x8100 outtpid 0x8100',
              'port-vlan 1 rule 1 untag add-vid inner-pri 0 inner-vid 4000 inner-tpid mode4 ether-type 0',
              'port-vlan 2 downstream inverse-upstream intpid 0x8100 outtpid 0x8100',
              'port-vlan 2 rule 1 untag add-vid inner-pri 0 inner-vid 4000 inner-tpid mode4 ether-type 0',
              'port-vlan 3 downstream inverse-upstream intpid 0x8100 outtpid 0x8100',
              'port-vlan 3 rule 1 untag add-vid inner-pri 0 inner-vid 4000 inner-tpid mode4 ether-type 0',
              'port-vlan 4 downstream inverse-upstream intpid 0x8100 outtpid 0x8100',
              'port-vlan 4 rule 1 untag add-vid inner-pri 0 inner-vid 4000 inner-tpid mode4 ether-type 0',
              'brief-show slot 1 interface gpon-olt 1/3  ont 1']
        #配置sfu绑定port_vlan......
        check_name='tips:配置sfu绑定port_vlan......'
        check_words=["port-vlan 1 rule 1",
                     'port-vlan 2 rule 1',
                     'port-vlan 3 rule 1',
                     'port-vlan 4 rule 1']
        output_lst=[]
        self.check_res1(cn,cmds,check_name,check_words,output_lst)

        self.logout_host()  

    @outer
    def clear_config(self):
        self.login_host()

        cn=sys._getframe().f_code.co_name
        cmds=['exit',
              'slot 1 interface gpon-olt 1/3',
              'no ont 2',
              'home',
              'slot 1',
              'no gpon profile flow 128 1',
              'no gpon profile tcont-bind 128 1',
              'no gpon profile tcont-svc 128',
              'no gpon profile dba 128',
              'brief-show slot 1 gpon profile']
        #将ONU恢复缺省配置......
        check_name='tips:将ONU恢复缺省配置......'
        check_words=['gpon profile flow id 128 1',
                     'gpon profile tcont-bind id 128 v-port 1',
                     'gpon profile tcont-svc id 128',
                     'gpon profile dba id 128']
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
    # telnet.clear_config()
    telnet.check_onu()
    telnet.uplink_config()
    telnet.downlink_config()
    telnet.profile_dba()
    telnet.profile_flow()
    telnet.profile_tcont_svc()
    telnet.profile_tcont_bind()
    telnet.svc_type()
    # telnet.port_vlan()
    # telnet.clear_config()
    #将标准输出和标准错误保存到log文件  
    sys.stdout,sys.stderr=output,output

#执行方式：python3 demo_office66_logfile.py
