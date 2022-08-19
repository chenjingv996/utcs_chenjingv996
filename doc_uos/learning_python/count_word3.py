#!/usr/bin/env python
#coding:utf-8
print("*"*60)
#统计字符个数
str=input("请输入一串字符:")
resoult={}
for i in str:
    resoult[i]=str.count(i)
print(resoult)
