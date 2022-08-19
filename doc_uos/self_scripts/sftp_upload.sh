#!/bin/bash
#远程上传文件测试
#if [ $# -ne 2 ]
#then
#	echo "miss arguments"
#	echo "need 2 arguments:BAT_DATE,SEQ_NO"
#	exit -1
#fi

#source $HOME/.bash_profile
#parameters
#BAT_DATE=$1  
#SEQ_NO=$2  

#定义变量
ftp_ip=10.20.53.172
ftp_user=uos
ftp_password=1
ftp_dir=/home/uos
GZ_DIR=/home/uuos/doc_chenjingv/script_cluster
send_file_name="ltp.py"

#执行文件上传命令
/usr/bin/expect <<-EOF
set timeout 10
spawn sftp $ftp_user@$ftp_ip
expect {
"*yes/no*" { send "yes\r"; exp_continue }
"*assword:" { send "$ftp_password\r" }
}
sleep 2

expect "sftp>"
send "lcd ${GZ_DIR}\r"
expect "sftp>" 
send "lpwd\r"

expect "sftp>" 
send "cd ${ftp_dir}\r"
expect "sftp>" 
send "pwd\r"

expect "sftp>" 
set timeout -1
send "put $send_file_name\r"

expect "sftp>" 
send "ls -lrt\r"
expect "sftp>"
send "quit\r"

expect eof
EOF
#SetCmdRslt $SEQ_NO 2
