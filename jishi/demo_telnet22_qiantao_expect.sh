#!/bin/bash

#set host_ip [lindex $argv 0]
#set ad "yuhong"
#set pw "yuhong"
#set pre_ip "192.168."
#set timeout 60
ad="yuhong"
pw="yuhong"
host_ip="192.168.$1"

/usr/bin/expect << EOF

set timeout 60

spawn telnet $host_ip

#expect "*gin:"
#send "$ad\r"
expect "*word:"
send "$pw\r"
sleep 1
expect "*>"
send "en\r"
expect "*word:"
send "$pw\r"
sleep 1
expect "*#"
send "conf t\r"
expect "*#"
send "show onuinfo gpon all\r"
expect "*#"
send "\r\r"

expect "*#"
send "show onu gpon autofind all\r"
expect "*#"
send "\r\r"

expect "*#"
send "int xgspon 0/3\r"
expect "*#"
send "show run\r"
expect "*#"
send "\r\r"

expect "*#"
send "int x-ethernet 0/3\r"
expect "*#"
send "show run\r"
expect "*#"
send "\r\r"

expect "*#"
send "exit\r"
expect "*#"
send "onu-lineprofile gpon profile-id 123\n"
expect "*#"
send "show run\n"
expect "*#"
send "\r\r"

expect "*#"
send "exit\r"
expect "*#"
send "onu-srvprofile gpon profile-id 123\n"
expect "*#"
send "show run\n"
expect "*#"
send "exit\r"

expect "*#"
send "show mac-addr vlan all\n"
expect "*#"
send "\r\r"

interact
expect eof
EOF

#执行方式：./demo.sh 10.123
