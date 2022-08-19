#!/usr/bin/env python
#coding:utf-8
import random
def get_twonum(start,end):
    while True:
        num1=random.randint(start,end)
        num2=random.randint(start,end)
        if num1<num2:
            return num1,num2
        elif num1>num2:
            return num2,num1

def is_prime_num(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def get_res(min,max):
    sum=0
    for i in range(min,max+1):
        if is_prime_num(i):
            sum+=i
    return sum




if __name__=="__main__":
    min_num,max_num=get_twonum(50,100)
    print("随机生成的2个数为:",min_num,max_num)
#    res=get_res(min_num,max_num)
    print("以上2个随机数之间的质数之和为:",get_res(min_num,max_num))
