#!/usr/bin/env python
#coding:utf-8
class Yunsuan:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def ji(self):
        return self.a*self.b
d1=Yunsuan(13,25)
print("以上2数之和为:",d1.add())
print("以上2数之积为:",d1.ji())
