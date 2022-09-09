#!/usr/bin/env python
#coding:utf-8

from functools import wraps

def hint(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('{} is running'.format(func.__name__))
        return func(*args,**kwargs)
    return wrapper


@hint
def hello123():
    print("hello,chenjingv!")



hello123()
