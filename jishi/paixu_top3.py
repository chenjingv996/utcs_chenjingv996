#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys,re,math

print(f"{time.ctime()}\n")
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')


class ccc:
    def aaa(self,arr:list)->int:
        if arr == None or len(arr) < 3:
            print("error!")
            return 
        r1 = r2 = r3 = i = 0
        while i < len(arr):
            if arr[i] > r1:
                r3 = r2 
                r2 = r1
                r1 = arr[i]
            elif arr[i] > r2 and arr[i] != r1:
                r3 = r2
                r2 = arr[i]
            elif arr[i] > r3 and arr[i] != r2:
                r3 =arr [i]
            i+=1
        return r1,r2,r3


bbb=ccc()

print(bbb.aaa([1,2]))
print(bbb.aaa([3,1,4,2,5,3,6]))


