#!/usr/bin/python3
#coding:utf-8


while True:
    try:
        l = input()
        for i in range(0, len(l), 8):
            print("{0:0<8s}".format(l[i:i+8]))
    except:
        break


