#!/usr/bin/expect -f

#set curr_time `date +%F\ %H:%M:%S`
set host_ip "192.168.3.123"
set ad "chenjingv"
set pw "123456"

set timeout -1

#echo -e "当前时间为:$curr_time\n"

#echo -e "`seq -s '#' 60|sed s/[0-9]//g`\n"

spawn ssh $ad@$host_ip

expect "*word:"
send "$pw\r"
expect "*$"
send "su\r"
expect "*:"
send "$pw\r"
expect "*#"
send "ip add\r"

interact


echo -e 
