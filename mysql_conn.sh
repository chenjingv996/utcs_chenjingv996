#!/bin/bash


curr_time=`date +%F\ %H:%M:%S`
host=192.168.3.123
user=root
pwd=123456

echo -e "`seq -s '#' 60|sed s/[0-9]//g`\n"
echo -e "${curr_time}\n"

mysql_conn()
{
mysql -u$user -p$pwd << EOF
use mysql;
select * from stus where tel like "%138%";
EOF

echo -e "\n\n"

}


mysql_conn
