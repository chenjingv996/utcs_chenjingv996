#!/usr/bin/env python
#coding:utf-8

class ccc:
    def aaa(self, x: int) -> int:
        str_num = str(x)
        if str_num[0] == '-':
            return -int(str_num[1:][::-1]) if int(str_num[1:][::-1]) < 2**31 else 0
        else:
            return int(str_num[::-1]) if int(str_num[::-1]) < 2**31-1 else 0



print(ccc().aaa(-12345))
print(ccc().aaa(-12340))
