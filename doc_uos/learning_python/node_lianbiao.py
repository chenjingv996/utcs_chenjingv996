#!/usr/bin/env python
#coding:utf-8
print("*"*60)
while True:
    try:
        n,nums,k=int(input()),input().split(),int(input())
        if k:
            print(nums[n-k])
        else:
            print(0)
    except:
        break
