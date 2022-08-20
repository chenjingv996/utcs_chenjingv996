#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        s=input()
        dic,res={},""
        for c in s:
            if c not in dic:
                dic[c]=1
            else:
                dic[c]+=1
        min_count=min(dic.values())
        for c in s:
            if dic[c]!=min_count:
                res+=c
        print(res)
    except:
        break
