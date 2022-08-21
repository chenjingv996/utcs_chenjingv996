#!/usr/bin/env python
#coding:utf-8
print("*"*60)
import datetime
while True:
    try:
        y,m,d=map(int,input().split())
        d=datetime.date(y,m,d)
        print(d.strftime("%j").lstrip("0"))
    except:
        break
