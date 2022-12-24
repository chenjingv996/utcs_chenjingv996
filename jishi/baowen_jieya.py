#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime as dt
import sys
import re
import math

print(f"{time.ctime()}\n")
print(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

class ccc:
    def aaa(self,s:str)->str:
#       str1=input().strip()
       i,stack,total=0,[],""
       while i<len(s):
           if s[i]=="]":
               tmp=""
               while stack:
                   value=stack.pop()
                   if value.isalpha():
                       tmp+=value
                   elif value.isdigit():
                       tmp=int(value)*tmp[::-1]
               else:
                   total+=tmp
           stack.append(s[i])
           i+=1
       return total
   

bbb=ccc()   
print(bbb.aaa("3[m]2[n]"))
   

print(f'\n')
