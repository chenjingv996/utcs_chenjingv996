#!/usr/bin/env python
#coding:utf-8

import paramiko
import time

client = paramiko.SSHClient()
client.load_system_host_keys()
 
# connect to client
client.connect("192.168.3.123",22,"chenjingv","123456",allow_agent=False,look_for_keys=False)
 
# get shell
ssh_shell = client.invoke_shell()
# ready when line endswith '>' or other character
while True:
    line = ssh_shell.recv(1024)
    #print line
    if line and line.endswith(b"$"):
        break;
 
# send command
ssh_shell.sendall("ping 192.168.3.123" + "\n")
 
# get result lines
lines = []
while True:
    line = ssh_shell.recv(1024)
    if line and line.endswith(b"\$"):
        break;
    lines.append(line)
result = ''.join(lines)
 
# print result
print (result)
