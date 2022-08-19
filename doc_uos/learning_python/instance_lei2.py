#!/usr/bin/env python
#coding:utf-8
print("*"*60)
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print("%s已经%d岁了!"%(self.name,self.age))

    def jump(self):
        print("%d岁的%s一直再跳!"%(self.age,self.name))
s1=Dog("小黑",8)
print(s1.name,s1.age)
s1.run()
s1.jump()
