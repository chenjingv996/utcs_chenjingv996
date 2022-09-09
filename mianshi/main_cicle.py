#!/usr/bin/env python
#coding:utf-8

PI=3.1415926

def get_zhouchang(radius):
    return 2*PI*radius

def get_area(radius):
    return PI*radius**2

def input_number():
    while True:
        input_str=input("请输入圆的半径:")
        try:
            input_num=float(input_str)
            return input_num
        except:
            print("输入数值不符合要求，请重新输入!")



if __name__=="__main__":
    number=input_number()
    zhouchang=get_zhouchang(number)
    area=get_area(number)
    print("圆的周长为:%.2f\t圆的面积为:%.2f"%(zhouchang,area))
    print(f'园的周长为:{zhouchang}\t园的面积为:{area}')




