#!/usr/bin/env python
#coding:utf-8 
name = raw_input('please enter your name: ')
print('hello,', name)
#str = raw_input()
#print("input string is: %s" % str)
x = raw_input('input a number: ')
num = int(x)
if num > 0:
    print("正数")
elif num == 0:
    print("零值")
else:
    print("负数")
#for i in range(0,5):
#    print i
def user(username):
    print("hello,"+username.title()+"!")
user('chenjingv')
