#!/usr/bin/env python
#coding:utf-8
print("*"*60)
res=int(input("请输入一个大于1的整数:"))
i=2
flag=True
while i<res:
    if res%i==0:
        flag=False
    i+=1
if flag:
    print(res,"是质数")
else:
    print(res,"不是质数")

