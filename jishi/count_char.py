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

def count_char():
    n=input()
    print(len(set(n)))


if __name__=="__main__":
    count_char()


print(f'\n')
