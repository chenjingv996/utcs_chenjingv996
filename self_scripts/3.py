#!/usr/bin/python3
#coding:utf-8

data = []
while True:
    try:
        n = input()
        ta = []
        for i in range(int(n)):
<<<<<<< HEAD
            ta.append(int(random.randint(1,500)))
=======
            ta.append(int(input()))
>>>>>>> f5d49cf25457c08b0f6a267f387120e6cb048f31
        uniq = set(ta)
        for j in sorted(uniq):
            print(j)
    except (EOFError, KeyboardInterrupt):
        break
