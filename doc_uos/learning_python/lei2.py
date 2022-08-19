#!/usr/bin/env python
#coding:utf-8
print("*"*60)
class Person:
    name="chenjingv"
    age=30
    def say_hello(self):
        print("你好,我是%s"%self.name)
p1=Person()
p2=Person()
print("$"*60)
p1.name="mayun"
p2.name="lijiacheng"
p1.say_hello()
p2.say_hello()
