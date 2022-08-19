#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from telnetlib import Telnet
Hosts=['172.30.111.254']
user='admin'
pwd='chenjingv123'
en='en'
finish='DSCC#'
commands=['show wireless','show wireless switch local status']
g_outfilePath='/home/test/out_logs'
def do_telnet(Hosts, user, pwd, finish, commands):
        tn = Telnet(Hosts, port=23, timeout=10)
        #tn.set_debuglevel(2)  

        # 输入登录用户名  
        tn.read_until('lgin:')  
        tn.write(user + '\n')  

        # 输入登录密码  
        tn.read_until('Password:')  
        tn.write(pwd + '\n')

        # 输入命令en  
        tn.read_until('DSCC>')  
        tn.write(en + '\n')


        tn.close() 
