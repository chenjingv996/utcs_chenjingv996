#!/usr/bin/env python
#coding:utf-8
def get_add(a,b):
    add=a+b
    return add

def get_mul(a,b):
    mul=a*b
    return mul
    
def input_number():
    while True:
        input_num1=float(input("请输入数值a:"))
        input_num2=float(input("请输入数值b:"))
        try:
            return input_num1,input_num2
        except:
            print("输入数值不符合要求，请重新输入!")


if __name__=="__main__":
    a,b=input_number()
    res1=get_add(a,b)
    print("以上2数之和为:%.2f"%res1)
    res2=get_mul(a,b)
    print("以上2数之积为:%.2f"%res2)
