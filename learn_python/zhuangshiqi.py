#!/usr/bin/env python
#coding:utf-8

print(f'"#"*60')

import time
#import datetime 

#print(f'当前时间为:{datetime.datetime.now()}')

def timer(func):
    def deco(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        stop = time.time()
        print(stop-start)
        return res
    return deco

@timer
def test(a):
    time.sleep(2)
    print("test is running!")
    return "bcd"

test()
