#!/usr/bin/env python
#coding:utf-8
print("*"*60)
a=input("请输入字符串:")
m=len(a)
b=list(a)
b.reverse()
c=list(a)
if b==c:
    print("该字符串是回文字符串！"+"其长度为%d"%m)
else:
    print("该字符串不是回文字符串!")
