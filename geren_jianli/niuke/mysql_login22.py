#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys
import re
import math
import pymysql

class mysql_oper:
    def mysql_connect():

    def mysql_select():

    def mysql_insert():

if __name__=="__main__":
    conn=pymysql.connect(host='192.168.3.123',
                         user='root', password='123456',
                         database='mysql', charset='utf8')    
    cur=conn.cursor()
    sql="select * from stus"
    cur.execute(sql)
    res=cur.fetchall()
    for i in res:
        print(i)
    cur.close()
    conn.close()
    #print(cur)
    print(f'\n')
