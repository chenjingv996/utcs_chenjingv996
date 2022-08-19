#!/bin/bash


ip=$(ip add | grep 'noprefixroute eno1'|awk '{print $2}'|awk -F '/' '{print $1}')
mac=$(ifconfig eno1 |grep ether|awk '{print $2}')
mask=$(ip add | grep 'noprefixroute eno1'|awk '{print $2}' |awk -F '/' '{print $2}')
gateway=$(ip route | grep via |awk '{print $3}')
dns1=$(grep nameserver /etc/resolv.conf |awk '{print $2}')
time=$(date "+%Y-%m-%d %H:%M:%S")
path=$(pwd)

touch $path/ip22.txt
chmod 777 $path/ip22.txt

printf "##########################################################\n">>ip22.txt
printf "current time:$time\n">>ip22.txt
printf "\n">>ip22.txt
printf "ip:$ip\n">>ip22.txt
printf "mac:$mac\n">>ip22.txt
printf "mask:$mask\n">>ip22.txt
printf "gateway:$gateway\n">>ip22.txt
printf "dns1:$dns1\n">>ip22.txt
printf "\n\n\n">>ip22.txt
#echo "dns2:$dns2"
