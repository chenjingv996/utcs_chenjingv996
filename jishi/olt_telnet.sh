#!/usr/bin/expect -f

set host_ip [lindex $argv 0]
set ad "chenjingv"
set pw "123456"
set timeout 60

spawn telnet $host_ip

expect "*gin:"
send "$ad\r"
expect "*ord:"
send "$pw\r"
sleep 1
expect "*:*"
send "su\r"
expect "*：*"
send "$pw\r"
sleep 1
expect "*#"
send "ip add\r"
expect "*#"
send "\r\r"

interact

