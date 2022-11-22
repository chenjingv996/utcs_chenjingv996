#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")


def paixu():
    res=[]
    for i in range(3):
        x=int(input(f"请输入第{i+1}个整数:"))
        res.append(x)
    res.sort()
    print(res)


if __name__=="__main__":
    paixu()


print(f'\n')
