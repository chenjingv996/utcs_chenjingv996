#!/usr/bin/env python
#coding:utf-8

import paramiko

hostname='192.168.0.123'

username='root'

password='123456'


if __name__=='__main__':

    paramiko.util.log_to_file('paramiko.log')
    
    s=paramiko.SSHClient()
    
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    s.connect(hostname = hostname,username=username, password=password)
    
    stdin,stdout,stderr=s.exec_command('ifconfig;free;df -h')
    
    print(stdout.read())
    
    s.close()

