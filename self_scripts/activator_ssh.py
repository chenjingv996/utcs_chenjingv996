#！/usr/bin/python3 
# -*- coding: utf-8 -*-

import paramiko
import sys

def su_root(host_ip,ssh_command):
    ssh = paramiko.SSHClient()
    key = paramiko.AutoAddPolicy()
    ssh.set_missing_host_key_policy(key)
    ssh.connect(hostname=  host_ip, port = 22, username='uos', password='1' ,timeout=5)
    stdin,stdout,stderr = ssh.exec_command(ssh_command)
    print (stdout.read().decode('utf-8').rstrip())

if __name__ == '__main__':
    if len(sys.argv) == 2:
        ssh_command = "uos-activator-cmd -s --kms kms.uniontech.com:8900:Vlc1cGIyNTBaV05v"
        host_ip = sys.argv[1]
        su_root(host_ip,ssh_command)
    else:
        print("参数错误")
