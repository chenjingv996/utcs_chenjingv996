#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import math

class ccc:
    def aaa(self,n:int)->int:
        cnt=0
        while n>=5:
            n//=5
            cnt+=n
        return cnt

print(ccc().aaa(5))

print(f'\n')
