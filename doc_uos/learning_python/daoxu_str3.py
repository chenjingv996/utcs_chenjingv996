#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        string = list(input().split())
        print(' '.join(string[::-1]))
    except:
        break