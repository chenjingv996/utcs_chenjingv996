#!/usr/bin/env python
#coding:utf-8
PI=3.1415926
def get_zhouchang(radius):
    return 2*PI*radius
def get_area(radius):
    return PI*radius**2

if __name__=="__main__":
    number=float(input("请输入圆的半径:"))
    zhouchang=get_zhouchang(number)
    area=get_area(number)
    print(float(zhouchang))
    print(float(area))
