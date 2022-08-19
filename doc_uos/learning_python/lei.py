#!/usr/bin/env python
#coding:utf-8
print("*"*60)
class Person:
    name="chenjingv"
    age=30
    def say_hello(self):
        print("hello!")
p1=Person()
p2=Person()
print(p1.name,p1.age)
print(p2.age,p2.name)
print("$"*60)
print(p1.say_hello)
p1.say_hello()
p2.say_hello()
p1.name="mayun"
p2.name="lijiacheng"
print(p1.name)
print(p2.name)
del p2.name
print(p2.name)
