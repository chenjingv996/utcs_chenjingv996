#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys
import re
import math

print(f"{time.ctime()}\n")
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

k=int(input())
h,s=input().strip().split('-',1)
s=''.join(s.split('-'))
for p in range(0,len(s),k):
    if len([i for i in s[p:p+k] if 'a'<=i<='z'])>len([i for i in s[p:p+k] if 'A'<=i<='Z']):
        h+='-'+s[p:p+k].lower()
    elif len([i for i in s[p:p+k] if 'a'<=i<='z'])<len([i for i in s[p:p+k] if 'A'<=i<='Z']):
        h+='-'+s[p:p+k].upper()
    else:
        h+='-'+s[p:p+k]
print(h)






print(f'\n')
