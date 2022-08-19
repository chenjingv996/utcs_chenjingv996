#!/usr/bin/env python
#coding:utf-8
print("*"*60)
a=input("请输入一组字符串:")
l=list(a)
print(l)
l.sort()
c=" ".join(l)
print("升序后的结果为:%s"%c)
print("*"*60)
l.sort(reverse=True)
b=" ".join(l)
print("降序后的结果为:%s"%b)
