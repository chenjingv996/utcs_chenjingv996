#!/usr/bin/expect -f

set host_ip [lindex $argv 0]
set pre_ip "172.17."
set ad "admin"
set pw "admin"
set term_len "no pause"
set timeout 60

spawn telnet $pre_ip$host_ip

expect "*gin:"
send "$ad\r"
expect "*word:"
send "$pw\r"
sleep 0.5
#expect "*>"
#send "en\r"
#expect "*word:"
#send "$pw\r"
#sleep 0.5

expect "*#"
send "$term_len\r"
send "\r\r"

expect "*#"
send "conf\r"
send "\r\r"

expect "*#"
send "brief-show slot 1 ont-info\r"
sleep 0.5
send "\r\r"

expect "*#"
send "brief-show slot 1 ont-unbound\r"
sleep 0.5
send "\r\r"

expect "*#"
send "brief-show vlan\r"
sleep 0.5
send "\r\r"

expect "*#"
send "brief-show vlan interface xge 3\r"
sleep 0.5
send "\r\r"

expect "*#"
send "brief-show port slot 4\r"
sleep 0.5
send "\r\r"

expect "*#"
send "brief-show vlan-translate\r"
sleep 0.5
send "\r\r"

expect "*#"
send "brief-show slot 1 interface gpon-olt 1/3\r"
sleep 0.5
send "\r\r"

expect "*#"
send "brief-show slot 1 interface gpon-olt 1/3 ont 1\r"
sleep 0.5
send "\r\r"

expect "*#"
send "brief-show slot 1 gpon profile  tcont-bind 127\r"
sleep 0.5
send "\r\r"

expect "*#"
send "brief-show slot 1 gpon profile  tcont-svc 127\r"
sleep 0.5
send "\r\r"

expect "*#"
send "brief-show slot 1 gpon profile  flow 127\r"
sleep 0.5
send "\r\r"

expect "*#"
send "brief-show mac-address vid 4000\r"
sleep 0.5
send "\r\r"
#send "exit\r"
#send "\r\r"

interact

#执行方式：./gpl116_oem_telnet.sh 10.135
