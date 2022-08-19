#!/usr/bin/env python
#coding:utf-8
print("*"*60)
class Person:
    name="chenjingv"
    age=30
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dog(self):
        print("你好,我是%s"%self.name)
p1=Person()
p2=Person()
p1.dog("xiaohei",30)
p2.dog("xiaobai",20)
