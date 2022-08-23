#!/usr/bin/python3
#coding:utf-8

data = []
while True:
    try:
        n = input()
        ta = []
        for i in range(int(n)):
            ta.append(random.randint(1,500))
        uniq = set(ta)
        for j in sorted(uniq):
            print(j)
    except (EOFError, KeyboardInterrupt):
        break
