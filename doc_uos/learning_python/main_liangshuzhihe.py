#!/usr/bin/env python
#coding:utf-8
def get_sum(a:int,b:int):
    sum=a+b
    return sum

def input_number():
    while True:
        input_num1=int(input("请输入数值a:"))
        input_num2=int(input("请输入数值b:"))
        try:
            return input_num1,input_num2
        except:
            print("输入数值不符合要求，请重新输入!")


if __name__=="__main__":
    a,b=input_number()
    res=get_sum(a,b)
    print("以上2数之和为:%d"%res)
