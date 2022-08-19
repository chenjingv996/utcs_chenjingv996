#!/usr/bin/env python
#coding:utf-8
print("*"*60)
a=input("请输入字符串:").lower()
s=""
for i in a:
    if i.isdigit() or i.isalpha():
        s+=i
if s[::-1]==s:
    print("True")
else:
    print("False")

