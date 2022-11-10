#!/usr/bin/env python
#coding:utf-8

PI=3.1415926


def get_zhouchang(radius):
    return 2*PI*radius

def get_area(radius):
    return PI*radius**2

def num():
    while True:
        input_str=input("请输入圆的半径:")
        try:
            input_num=float(input_str)
            return input_num
        except:
            print("输入有误，请重新输入!")



if __name__=="__main__":
    number=num()
    zhouchang=get_zhouchang(number)
    area=get_area(number)
    print("\n"+str(float(zhouchang))+"\n")
    print("\n"+str(float(area))+"\n")
