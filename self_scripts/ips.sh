#!/bin/bash


ip=$(ip add | grep 'noprefixroute eno1'|awk '{print $2}'|awk -F '/' '{print $1}')
mac=$(ifconfig eno1 |grep ether|awk '{print $2}')
mask=$(ip add | grep 'noprefixroute eno1'|awk '{print $2}' |awk -F '/' '{print $2}')
gateway=$(ip route | grep via |awk '{print $3}')
dns1=$(grep nameserver /etc/resolv.conf |awk '{print $2}')
path=$(pwd)

touch $path/ip.txt
chmod 777 $path/ip.txt

echo "##########################################################">>ip.txt
echo "ip:$ip">>ip.txt
echo "mac:$mac">>ip.txt
echo "mask:$mask">>ip.txt
echo "gateway:$gateway">>ip.txt
echo "dns1:$dns1">>ip.txt
printf "\n\n\n">>ip.txt
#echo "dns2:$dns2"
