#!/usr/bin/env python
#coding:utf-8
print("*"*60)
f=open("/home/chenjingv/demo.txt",mode="r",encoding="utf-8")
content=f.read()
print(content)
f.close()
