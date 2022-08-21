#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        s=input()
        l=[0,0,0]
        for i in s:
            l[0]+=int(i.isalpha())
            l[1]+=int(i.isspace())
            l[2]+=int(i.isnumeric())
        print("字母个数为:",l[0])
        print("空格个数为:",l[1])
        print("数字个数为:",l[2])
        print("特殊字符个数为:",len(s)-l[0]-l[1]-l[2])
    except:
        break
