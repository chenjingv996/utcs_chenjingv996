#!/usr/bin/env python
#coding:utf-8
import os
os.system("ifconfig | grep -A3 ens")
name=raw_input('please enter your name:')
#print 'hello,',name
message="chenjingv"
#print message
print (60*'*')
print (60*"$")
print (100+200)
abc="shen zhou shu ma chenjingv"
print abc.title()
print abc.upper()
print abc.lower()
print ('python23456')
print ('\tpython12345')
cars=['bmw','audi','subaru','honda']
#len(cars)
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
#print cars
cars.reverse()
print cars
for value in range(1,9):
    print(value)
    print(list(range(1,5)))
nos=list(range(1,7))
print nos

sqares=[]
for value in range(1,21):
#    sqare=value**2
    sqares.append(value**2)
print(sqares)

age=12
if age<4:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
elif age>=65:
    price=5
print("your admission cost is $"+str(price)+".")

x=1
while x<=5:
    print(x)
    x+=1



def gt_users(names):
    for name in names:
        msg = "hello, "+name.title()+"!"
        print(msg)
usernames = ['chenjingv','mayun','xijingpin']
gt_users(usernames)
