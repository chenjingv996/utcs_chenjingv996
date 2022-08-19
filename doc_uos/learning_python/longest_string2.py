#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        a, b = input(), input() # a保存短，b保存长
        if len(a) > len(b):
            a, b = b, a
        res = ''
        for i in range(0, len(a)):
            for j in range(i+1, len(a)):
                if a[i:j+1] in b and j+1-i > len(res):
                    res = a[i:j+1]
        print(res)
    except:
        break
