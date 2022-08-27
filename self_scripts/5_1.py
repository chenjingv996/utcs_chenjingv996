#!/usr/bin/python3
#coding:utf-8

while True:
    try:
        temp = input()
        while(len(temp)>0):
            print(temp[:8].ljust(8,"0"))
            temp = temp[8:]
    except:
        break

