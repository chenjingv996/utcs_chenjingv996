#!/usr/bin/env python
#coding:utf-8
while True:
    try:
        s = input()
        res = []
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    res.append(j-i)
        if res != '':
            print(max(res))
    except:
        break