#!/usr/bin/env python
#coding:utf-8
print("*"*60)
def fun(num):
    temp=list(num)
    temp.reverse()
    str1="".join(temp)
    print(str1)
fun(input())
