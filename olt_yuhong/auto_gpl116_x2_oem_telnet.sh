#!/usr/bin/expect -f

set host_ip [lindex $argv 0]
set ad "yuhong"
set pw "yhkt@123"
set term_len "terminal page-break disable"
set pre_ip "172.17."
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

expect "*#"
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
send "exit\r"
send "\r\r"

expect "*#" 
sleep 0.5
send "show run int ten-gigabitethernet 1/2\r"
send "\r\r"

expect "*#"
sleep 0.5
send "show run int gpon-olt 3/3\r"
send "\r\r"

expect "*#"
sleep 0.5
send "show mac-address-table l2-address vlan 4000\r"
send "\r\r"

interact

#执行方式：./local_olt_telnet.sh 8.200
