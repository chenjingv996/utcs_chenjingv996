#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys,re,math

print(f"{time.ctime()}\n")
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')


class ccc:
    def aaa(self,lst:list)->list:
        n=len(lst)
        for i in range(n):
            for j in range(1,n-i):
                if lst[j-1]>lst[j]:
                    lst[j-1],lst[j]=lst[j],lst[j-1]
        return lst

bbb=ccc()
print(bbb.aaa([3,1,4,2]))
print()


