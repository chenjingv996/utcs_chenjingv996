#!/usr/bin/expect -f

set host_ip [lindex $argv 0]
set pre_ip "172.17."
set ad "admin"
set pw "admin123"
set term_len "terminal page-break disable"
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
send "$term_len\r"

expect "*#"
send "show version\r"
send "\r\r"

expect "#"
send "conf t\r"
send "\r\r"

expect "*#"
sleep 0.5
send "show interface gpon-olt illegal-onu\r"
send "\r\r"

expect "*#"
sleep 0.5
send "show gpon-onu information\r"
send "\r\r"

expect "*#"
sleep 0.5
send "show interface gpon-onu creation-information\r"
send "\r\r"

expect "*#"
sleep 0.5
send "show interface gpon-onu online-information\r"
send "\r\r"

expect "*#" 
sleep 0.5
send "show dba-profile 500\r"
send "\r\r" 

expect "*#"
sleep 0.5
send "show gpon-onu-line-profile 500\r"
send "\r\r"

expect "*#"
sleep 0.5
send "show gpon-onu-service-profile 500 | section-end WLAN\r"
send "\r\r"

expect "*#" 
sleep 0.5
send "end\r"
send "show mac-address-table l2-address vlan 120\r"
send "\r\r"

expect "*#"
sleep 0.5
send "show gpon-onu information\r"
send "\r\r"

expect "*#"
send "conf t\r"
send "\r\r"
send "int ten-gigabitethernet 10/1\r"
send "\r\r"
send "show interface ten-gigabitethernet 10/1 ddm information\r" 
send "\r\r"

expect "*#"
sleep 0.5
send "exit\r"
send "\r\r"
send "int gpon-olt 3/3\r"
send "\r\r"
send "show interface gpon-olt 3/3 illegal-onu\r"
send "\r\r"
send "show interface gpon-onu creation-information | in 3/3\r"
send "\r\r"
send "show interface gpon-onu online-information | in 3/3\r"
send "\r\r"

expect "*#"
sleep 0.5
send "exit\r"
send "\r\r"

interact

#执行方式：./gpl116_oem_telnet.sh 10.135
