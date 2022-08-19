#!/usr/bin/env python
#coding:utf-8
print("*"*60)
x,y,z = input(),input(),input()
print(*sorted(y.split(' '),key=int,reverse=bool(int(z))))
