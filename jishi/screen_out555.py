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

def screen_end(s):
    screen = ''
    clip = ''
    selected = False
    for i in s:
        if i == '1' and not selected:  # a
            screen += 'a'
        elif i == '1' and selected:  # a
            screen = 'a'
            selected = False
        elif i == '2' and selected and screen:  # ctrl-c
            clip = screen
        elif i == '3' and selected and screen:  # ctrl-x
            clip = screen
            screen = ''
            selected = False
        elif i == '4' and selected:  # ctrl-v
            screen = clip
            selected = False
        elif i == '4' and not selected:  # ctrl-v
            screen += clip
        elif i == '5' and screen:  # ctrl-a
            selected = True
    return len(screen)


print(screen_end("11515244"))
print(screen_end("111"))


print(f'\n')
