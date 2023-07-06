#!/usr/bin/expect -f

set host_ip [lindex $argv 0]
set ad "yuhong"
set pw "yuhong"
set pre_ip "192.168."

set timeout 60


spawn telnet $pre_ip$host_ip

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
send "show time\r"
expect "*#"
send "\r\r"

send "show image loading-status\r"
expect "*#"
send "\r\r"

send "conf t\r"
expect "*#"
send "show onuinfo xgspon all\r"
expect "*#"
send "\r\r"

expect "*#"
send "show onu xgspon autofind all\r"
expect "*#"
send "\r\r"

expect "*#"
send "show run | in add\r"
expect "*#"
send "\r\r"

expect "*#"
send "int xgspon 0/3\r"
expect "*#"
send "show run\r"
expect "*#"
send "\r\r"

expect "*#"
send "int x-ethernet 0/8\r"
expect "*#"
send "show run\r"
expect "*#"
send "\r\r"

expect "*#"
send "exit\r"
expect "*#"
send "dba-profile profile-id 123\n"
expect "*#"
send "show run\n"
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
send "\r\r"
send "exit\r"

expect "*#"
send "show dba-profile all\n"
expect "*#"
send "\r\r"

send "show traffic-profile all\n"
expect "*#"
send "\r\r"

send "show mac-addr vlan 100\n"
expect "*#"
send "\r\r"

interact

#执行方式：./chenjingv_gxl116_develop_telnet.sh 10.123
