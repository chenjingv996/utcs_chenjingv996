#!/usr/bin/env python
#coding:utf-8
class Rec:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
d1=Rec(3,5)
print("该矩形面积为:",d1.area())
