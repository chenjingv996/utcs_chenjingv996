#!/usr/bin/env python
#coding:utf-8


def get_sum(num):
    sum=0
    i=1
    while i<=num:
        sum=sum+i
        i=i+1
    return sum


if __name__=="__main__":
    print("1到100之和为:%d"%get_sum(100))


