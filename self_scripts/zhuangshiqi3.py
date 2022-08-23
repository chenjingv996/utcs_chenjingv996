#!/usr/bin/env python
#coding:utf-8

print("#"*80)
    
def fn():
    print("我是fn函数!")

def add(a,b):
    r=a+b
    return r

def mul(a,b,c):
    print(a*b*c)
#    return r

def begin_end(old):
    def new_fun(*args,**kwargs):
        print("执行开始...")
        res=old(*args,**kwargs)
#        return res
        print("执行结束...")
        return res
    return new_fun

f3=begin_end(mul)
r3=f3(2,3,4)

print(r3)

