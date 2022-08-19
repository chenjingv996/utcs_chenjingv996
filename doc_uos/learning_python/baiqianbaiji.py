#!/usr/bin/env python
#coding:utf-8
print("*"*60)
test=input()
for i in range(100):
    for j in range(100-i):
        if 5*i+3*j+(100-i-j)/3==100:
            print(str(i)+" "+str(j)+" "+str(100-i-j))

