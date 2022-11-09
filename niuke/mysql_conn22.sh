#!/bin/bash
# 连接mysql数据库，并查询结果，将结果输出到文件中
# 1.定义连接变量
mysql_u="root"
mysql_p="123456"
save_f="mysql.txt"
save_p="/home/chenjingv/utcs_chenjingv996/niuke/"
mysql_sq="select * from stus"
export MYSQL_PWD=${mysql_p}
echo "开始链接数据库..."
# 2.连接数据库
result=`mysql -u$mysql_u << EOF
use mysql;
$mysql_sq;
quit
EOF`
# 判断是否连接成功
if [ $? = 0 ]
then
 echo "连接成功..."
else
 echo "连接失败..."
 exit
fi
echo "写入查询结果..."
# 将结果写入文本
echo "$result" >> $save_p$save_f
echo "写入完成..."
