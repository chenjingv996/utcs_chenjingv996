#!/usr/bin/env python
#coding:utf-8

nums=[int(i) for i in input().strip().split(',')]
#print(nums)   #debug
k=int(input())
l,r=0,k
n=len(nums)
res=sum(nums[0:k])
ans=res
while r<n:
    ans+=nums[r]
    ans-=nums[l]
    r+=1
    l+=1
    res=max(res,ans)
    print(ans)   #debug
print(res)

