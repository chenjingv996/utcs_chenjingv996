#!/usr/bin/env python
#coding:utf-8
print("*"*60)
def huiwen(s):
    if len(s)<2:
        return True
    elif s[0]!=s[-1]:
        return False
    return huiwen(s[1:-1])

if __name__=="__main__":
    str1=input("请输入一组字符串:")
    res=huiwen(str1)
    print (res)


