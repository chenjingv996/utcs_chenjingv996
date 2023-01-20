#!/usr/bin/env python
#coding:utf-8

import re

class ccc:
    def aaa(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


print(ccc().aaa("-3412fewfwe45+rege36"))

