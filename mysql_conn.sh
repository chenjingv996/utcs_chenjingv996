#!/bin/bash

curr_time=`date +%F\ %T`

echo -e "\n当前时间为:${curr_time}\n"
echo -e "$(date +%F\ %T)\n"


systemctl status mysql
echo -e "q\n"

netstat -nap |grep :3306
echo -e "\n"

mysql -h 192.168.3.123 -u root -p
echo -e "123456\n"
echo -e "show databases;\n"

