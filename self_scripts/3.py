#!/usr/bin/python3

try:
    n = input()
    ta = []
    for i in range(int(n)):
        ta.append(int(input()))
    for j in sorted(set(ta)):
        print(j)
except:
    break

