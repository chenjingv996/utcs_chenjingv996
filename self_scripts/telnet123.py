#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telnetlib
import re
import time
HOST = '172.22.9.31'
user = 'admin'
password = 'admin'
#en = 'en'
#su = 'su'
#reboot = 'reboot'
tn = telnetlib.Telnet(HOST)
tn.read_until("login: ")
tn.write(user + "\n")
tn.read_until("Password: ")
tn.write(password + "\n")
time.sleep(1)

tn.write(en + "\n")
time.sleep(1)

tn.write('show wireless mana' + "\n")
time.sleep(1)

#print (tn.read_all())
tn.close()
