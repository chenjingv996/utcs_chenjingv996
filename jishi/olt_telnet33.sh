#!/usr/bin/expect -f

set host_ip [lindex $argv 0]
set ad "chenjingv"
set pw "123456"
set timeout 60

spawn telnet $host_ip

expect {
"*gin:"
{send "$ad\r";exp_continue}
"*ord:"
{send "$pw\r";exp_continue}
sleep 1
"*:*"
{send "su\r";exp_continue}
"*：*"
{send "$pw\r"}
sleep 1
"*#"
{send "ip add\r"}
"*#"
{send "\r\r"}
}

interact

