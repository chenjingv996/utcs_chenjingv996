#!/usr/bin/expect -f

set host_ip [lindex $argv 0]
set ad "chenjingv"
set pw "123456"
set pre_ip "192.168."

set timeout 60


spawn telnet $pre_ip$host_ip

expect "*gin:"
send "$ad\r"

expect "*word:"
send "$pw\r"
sleep 1

expect "*:*"
send "su\n"

expect "*：*"
send "$pw\r"
sleep 1

expect "*#"
send "ip add\r"

expect "*#"
send "cd ./utcs_chenjingv996/jishi\r"

#expect "*#"
#send "\r\r"
#
#expect "*#"
#send "show onu gpon autofind all\r"
#expect "*#"
#send "\r\r"
#
#expect "*#"
#send "int xgspon 0/3\r"
#expect "*#"
#send "show run\r"
#expect "*#"
#send "\r\r"
#
#expect "*#"
#send "int x-ethernet 0/3\r"
#expect "*#"
#send "show run\r"
#expect "*#"
#send "\r\r"
#
#expect "*#"
#send "exit\r"
#expect "*#"
#send "onu-lineprofile gpon profile-id 123\n"
#expect "*#"
#send "show run\n"
#expect "*#"
#send "\r\r"
#
#expect "*#"
#send "exit\r"
#expect "*#"
#send "onu-srvprofile gpon profile-id 123\n"
#expect "*#"
#send "show run\n"
#expect "*#"
#send "exit\r"
#
#expect "*#"
#send "show mac-addr vlan all\n"

expect "*#"
send "\r\r"

interact

#执行方式：./demo.sh 8.200
