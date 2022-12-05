#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime
import sys
import re
import math

print(f"{time.ctime()}\n")
print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')


# 2022/3/14 13:05 - 时间
# PyCharm - 当前集成开发环境
# 密码要求:
# 1.长度超过8位
# 2.包括大小写字母.数字.其它符号,以上四种至少三种
# 3.不能有长度大于2的不含公共元素的子串重复 （注：其他符号不含空格或换行）
# 练习
def mima(arr:str)->bool:
    if len(arr)<=8:
        return False
    else:
        flag = [0,0,0,0] # 标记位
        for i in arr:
            if 'a'<=i<='z':
                flag[0]=1
            elif 'A'<=i<='Z':
                flag[1] = 1
            elif i.isdigit():
                flag[2] = 1
            else:
                flag[3] = 1
        if sum(flag)<3: #标记位数＜3就说明是不够
            return False
        else:
            for i in range(len(arr)-3):
                if arr[i:i+3] in arr[i+3:]:# 切割字符串 如果有说明是重复了
                    return False
            return True
while 1 :
    try:

        s = input()
        if mima(s) is True:
            print("OK")
        else:
            print("NG")
    except:
        break



print(f'\n')
