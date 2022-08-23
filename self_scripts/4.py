#!/usr/bin/python3
#coding:utf-8

n = input()
random_num_list = []
for _ in range(int(n)):
    random_num = input()
    random_num_list.append(int(random_num))
r = list(set(random_num_list))
r.sort()
for i in r:
	print(i)
