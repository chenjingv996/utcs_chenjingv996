#!/usr/bin/env python
#coding:utf-8

import random

num=random.randint(1,101)
print(num)
n=int(input())

if n>num:
    print("猜大了!")
elif n<num:
    print("猜小了!")
else:
    print("恭喜你，猜对了!")
