#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys
import re
import math



class ccc:
    def aaa(self, s: str) -> int:
        length = 0
        queue = []
        for i in s:
            if i in queue:
                length = max(length, len(queue))
                while i in queue:
                    queue.pop(0)
            queue.append(i)
        return max(length, len(queue))


print(ccc().aaa("abcdadaef"))
print(ccc().aaa(""))
print(ccc().aaa("ddd"))



print(f'\n')
