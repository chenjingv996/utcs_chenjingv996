#!/usr/bin/env python
#coding:utf-8
str1=input("请输入一组字符串:")
str2=str1.split(" ")
for i in str2[::-1]:
    print(i,end=" ")
print()

