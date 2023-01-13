#!/usr/bin/python env
#coding:utf-8

import time
import datetime
import paramiko
import telnetlib3
import sys
import re

def connect_sw(host):
    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko,AuthAddPolicy())
    try:
        ssh.connect(host,22,username='chenjingv',password='123456')
        return ssh
    expect:
        print("remote connection failed!")


if __name__=="__main__":
    print(connet_sw("192.168.3.123"))

#执行方式：./demo.sh 8.200
