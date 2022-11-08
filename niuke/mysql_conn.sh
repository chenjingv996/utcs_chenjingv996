#!/bin/bash

echo -e "######################################################\n"

curr_time=`date +%F\ %H:%M:%S`
host=192.168.3.123
user=root
pwd=123456

mysql -u$user -p$pwd << EOF
use mysql;
select * from stus;
EOF

echo -e "${curr_time}\n"

echo -e "$(date +%F_%T)\n"

echo -e "`date +%F\ %H:%M:%S`\n"

echo -e "\n"
