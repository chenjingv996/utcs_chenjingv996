#!/usr/bin/expect -f

set host_ip [lindex $argv 0]
set pre_ip "192.168."
set ad "yuhong"
set pw "yhkt@123"
set timeout 60

spawn telnet $pre_ip$host_ip

expect "*gin:"
send "$ad\r"
expect "*word:"
send "$pw\r"
sleep 0.5
expect "*>"
send "en\r"
expect "*word:"
send "$pw\r"
sleep 0.5

expect "*#"
send "show version\r"
send "\r\r"

expect "#"
send "conf t\r"
send "\r\r"

expect "*#"
send "end\r"
send "show interface gpon-olt illegal-onu\r"
send "\r\r"

expect "*#"
#send "end\r"
send "show gpon-onu information\r"
send "\r\r"

expect "*#"
#send "end\r"
send "show interface gpon-onu creation-information\r"
send "\r\r"

expect "*#"
#send "end\r"
send "show interface gpon-onu 3/5/1 online-information\r"
send "\r\r"

expect "*#" 
#send "end\r"
send "show dba-profile 500\r"
send "\r\r" 

expect "*#"
#send "end\r"
send "show gpon-onu-line-profile 500\r"
send "\r\r"

expect "*#"
#send "end\r"
send "show gpon-onu-service-profile 500\r"
expect "*--"
send "q"
send "\r\r"

expect "*#" 
#send "end\r"
send "show mac-address-table l2-address vlan 100\r"
send "\r\r"

expect "*#"
#send "end\r"
send "show gpon-onu information\r\r"

expect "*#"
#send "end\r"
send "conf t\r"
send "int ten-gigabitethernet 1/1\r"
send "show interface ten-gigabitethernet 1/1 ddm information\r\r" 

expect "*#"
send "end\r"
send "conf t\r"
send "int gpon-olt 3/5\r"
send "show interface gpon-olt 3/5 illegal-onu\r\r"

expect "*#"
send "end\r"
#send "conf t\r"
#send "int gpon-olt 3/5\r"
send "show mac-address-table l2-address vlan 100\r\r"
send "\r\r"

interact

#执行方式：./gpl116_oem_telnet.sh 10.135
