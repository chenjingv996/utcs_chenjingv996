#!/usr/bin/env python
#coding:utf-8
print(60*"#")
string = input().lower()
word = input().lower()
times = 0
for w in string:
        if w == word:
                    times = times + 1
                    print(times)
