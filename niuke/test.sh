#!/bin/bash


curr_time=`date +%F\ %H:%M:%S`

echo -e "`seq -s '#' 60|sed s/[0-9]//g`\n"

echo -e "${curr_time}\n"

echo -e "$(date +%F_%T)\n"

echo -e "`date +%F\ %H:%M:%S`\n"

echo -e "计算结果为:`expr 3 \* 30`"

echo -e "计算结果为:`expr 3 + 30`"

echo -e "\n"
