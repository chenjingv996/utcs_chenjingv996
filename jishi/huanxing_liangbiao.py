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
    def aaa(self, head: ListNode) -> bool:
        # 1. python map
        m = {}
        while head:
            if m.get(head):
                return True
            m[head] = 1
            head = head.next
        return False





print(f'\n')
