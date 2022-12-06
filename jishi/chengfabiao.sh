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


#!/bin/bash
 
for i in `seq  9`
do
    for j in `seq  $i`       #这地方写成$i 就比写成seq 9 方便多了呢
    do
        echo  -n  "$i*$j=$(($i*$j)) "    #有一个空格
    done
    echo             内层循环完成以后换行
done
echo



print(f'\n')
