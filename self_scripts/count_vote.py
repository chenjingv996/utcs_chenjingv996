#!/usr/bin/env python
#coding:utf-8
print("*"*60)


while True:
    try:
        n=int(input("输入候选人个数:"))
        name_lst=input("输入候选人名字:").split()
        m=int(input("输入投票人数:"))
        vote_lst=input("输入投票结果:").split()
        valid_count=0
        
        
        for i in name_lst:
            valid_count+=vote_lst.count(i)
            print(i+" : "+str(vote_lst.count(i)))
        print("invalid : "+str(m-valid_count))


    except:
        break
