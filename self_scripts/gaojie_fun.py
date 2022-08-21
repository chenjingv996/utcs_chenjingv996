#!/usr/bin/env python
#coding:utf-8

lst=[1,2,3,4,5,6,7,8,9,10]

#取偶数
def fn2(i):
    if i%2==0 :
        return True
    return False

#取大于5的数
def fn3(i):
    if i>5 :
        return True
    return False

def fn(func,lst):
    new_lst=[]
    for n in lst:
        if func(n):
            new_lst.append(n)
    return new_lst

print(fn(fn3,lst))
print(fn(fn2,lst))
print("hello,chenjingv!")
