#!/usr/bin/expect -f


set host_ip [lindex $argv 0]
set pre_ip "192.168."
set ad "admin"
set pw "admin123"
set timeout 60

spawn telnet $pre_ip$host_ip

expect "*gin:"
send "$ad\r"
expect "*word:"
send "$pw\r"
sleep 1
expect "*>"
send "en\r"
expect "*word:"
send "$pw\r"
sleep 1

expect "*#"
send "conf t\r\r"

expect "*#"
send "show onu state\r\r"

expect "*#"
send "show onu info\r\r"

expect "*#"
send "show mac address-table\r\r"

expect "*#"
send "int gigabitethernet 0/3\r"
send "show run int\r\r"

expect "*#"
send "int gpon 0/5\r"
send "show run int\r\r"
send "show run onu 1\r\r"

expect "*#"
send "exit\r"
send "show ip igmp snooping config\r\r"



interact

#执行方式：./gpl116_oem_telnet.sh 10.135
