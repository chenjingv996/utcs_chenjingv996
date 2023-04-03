#!/usr/bin/env python
#coding:utf-8

str1="qwert"
lst1=["q","w","e"]
lst2=["a","q","e"]

for i in range(len(lst1)):
    if lst1[i] not in str1:
        print("fail")
        break
else:
    print("pass")

for i in range(len(lst2)):
    if lst2[i] not in str1:
        print("fail")
        break
else:
    print("pass")

