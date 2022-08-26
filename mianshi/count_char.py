#!/usr/bin/env python
#coding:utf-8


str1=input()
str2=str1.lower()
char1=input()
char2=char1.lower()
num=str2.count(char2)


def count_char():
    if 1<=len(str1)<=10:
        if char2 in str2:
            print(num)    
        else:
            print("不存在该字符!")
    else:
        print("字符串过长!")




if __name__=="__main__":
    count_char()


