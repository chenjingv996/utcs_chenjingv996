#!/usr/bin/python3
#coding:utf-8

data = []
while True:
    try:
        n = input()
        ta = []
        for i in range(int(n)):
            ta.append(int(input()))
        uniq = set(ta)
        for j in sorted(uniq):
            print(j)
    except (EOFError, KeyboardInterrupt):
        break
