#!/usr/bin/python3
#coding:utf-8

import random

data = []
while True:
    try:
        n = input()
        ta = []
        for i in range(int(n)):
            ta.append(int(random.randint(1,500))
        uniq = set(ta)
        for j in sorted(uniq):
            print(j)
    except (EOFError, KeyboardInterrupt):
        break
