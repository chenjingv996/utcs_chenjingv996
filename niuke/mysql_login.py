#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys
import re
import math
import pymysql

conn=pymysql.connect(host='192.168.3.123',
        user='root', password='123456',
        charset='utf8')
cur=conn.cursor()
print(cur)

print(f'\n')
