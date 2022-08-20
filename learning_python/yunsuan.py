#!/usr/bin/env python
#coding:utf-8
print(60*"*")
i=0
j=0
while i<100:
    i+=1
    j+=i
print("1到100的和为:%d"%j)
print("$"*60)
aaa=sum(range(1,101))
print("1到100的和为:%d"%aaa)
input("1到100的和为:%d"%sum(range(101)))
print(sum(range(101)))
print("以上两数之和为:"+str(int(input("请输入数字a:"))+int(input("请输入数字b:"))))
print("以上两数之积为:"+str(int(input("请输入数字c:"))*int(input("请输入数字d:"))))
print("该字符串长度为:"+str(len(str(input("请输入字符串:")))))
