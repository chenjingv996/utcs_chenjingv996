#!/usr/bin/env python
#coding:utf-8
print("*"*60)
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print("%s在一直奔跑!"%self.name)
s1=Dog("小黑",8)
s1.run()
print(s1.name,s1.age)
