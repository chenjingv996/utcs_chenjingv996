#!/usr/bin/env python
#coding:utf-8
print("*"*60)
import math
 
max = 100  # 设定范围, a,b,c都在100以内
pn = []  # Pythagorean Number 勾股数
for a in range(2, int(max//math.sqrt(2))+1):
    for b in range(a+1, int(math.sqrt(max*max - a*a))+1, 2):         
        c = int(math.sqrt(s := a*a + b*b))
        if c*c == s and math.gcd(a,b) == 1:
            pn.append((a, b, c))
for t in pn:
    print(t)
print(f"Total = {len(pn)}")