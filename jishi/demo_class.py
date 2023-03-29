#!/usr/bin/env python
#coding:utf-8

import time
import sys
import paramiko

from telnetlib import Telnet
import csv

class main:
    def __init__(self):
        self.success=open('success.csv','a',encoding='utf-8',newline='')
        self.failure=open('failure.csv','a',encoding='utf-8',newline='')
        self.success_writer=csv.writer(self.success)
        self.failure_writer=csv.writer(self.failure)

    def telnet(self,ip, port):
        """
        测试单个ip和端口是否能连通
        """
        try:
            tn=Telnet(host=ip, port=port, timeout=2)
            print( f"{ip} {port} 端口开放")
            row=[ip,port,'端口开放']
            self.success_writer.writerow(row)
            tn.close()
        except:
            row=[ip,port,'端口未开放，无法连通']
            self.failure_writer.writerow(row)
            print(f"{ip} {port}  端口未开放，无法连通")

    def GetIpAndPort(self):
        """
        从文件中逐行读取ip和端口
        """
        #注意ip和端口末尾的换行符及可能有空行的情况产生
        with open('ips.txt','r',encoding='utf-8') as file:
            ips=file.readlines()
        
        with open('ports.txt','r',encoding='utf-8') as file:
            ports=file.readlines()
        return ips,ports
        
if __name__ == '__main__':
    main=main()
    ips,ports=main.GetIpAndPort()
    for i in range(len(ips)):
        ip=ips[i].strip()
        port=ports[i].strip()
        if ip=='' or port =='':
            continue
        else:
            main.telnet(ip,port)
    print('执行完毕!')
    main.success.close()
    main.failure.close()
