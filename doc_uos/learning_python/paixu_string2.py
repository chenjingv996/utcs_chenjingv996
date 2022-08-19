#!/usr/bin/env python
#coding:utf-8
print("*"*60)
n=int(input("请输入n组字符串:"))
lst1=[]
for i in range(n):
    str1=input()
    lst1.append(str1)
lst1.sort()
print("\n".join(lst1))
