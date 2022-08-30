#!/usr/bin/env python
#coding:utf-8

class ccc:
    def aaa(self,x:int)->bool:
        if str(x)==str(x)[::-1]:
            return True
        else:
            return False

print(ccc().aaa(12321))
p1=ccc()
print(p1.aaa(-1234))
print(p1.aaa("abcba"))
print(p1.aaa(1221))

