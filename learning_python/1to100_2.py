#!/usr/bin/env python
#coding:utf-8


def get_sum(num):
    sum=0
    for i in range(num+1):
        sum=sum+i
    return sum


if __name__=="__main__":
    print("1到100之和为:%d"%get_sum(100))


