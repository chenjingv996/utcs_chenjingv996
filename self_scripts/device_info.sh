#!/bin/bash


ip=$(ip add | grep 'dynamic'|awk '{print $2}'|awk -F '/' '{print $1}')
current_time=$(date "+%Y-%m-%d %H:%M:%S")
device_name=$(sudo lscpu | awk '/Vendor ID/ {print $NF}')
mem_info=$(sudo free -m)
disk_info=$(sudo fdisk -l)
device_info=$(sudo dmidecode)
path=$(sudo pwd)
version=$(sudo uname -a)


if [ -f $path/device_$device_name.txt ]
then
    echo  "the file is exist,remove it......"
    rm -rf $path/device_$device_name.txt
else
    echo  "the file is not exist,create it......"
    touch $path/device_$device_name.txt 
    chmod 777 $path/device_$device_name.txt
fi

printf "###############################################################################################################\n">>$path/device_$device_name.txt

printf "current_time:\n$current_time\n\n">>$path/device_$device_name.txt

printf "version:\n$version\n\n">>$path/device_$device_name.txt

printf "ip:\n$ip\n\n">>$path/device_$device_name.txt

printf "mem_info:\n$mem_info\n\n">>$path/device_$device_name.txt

printf "disk_info:\n$disk_info\n\n">>$path/device_$device_name.txt

printf "device_info:\n$device_info\n\n">>$path/device_$device_name.txt

printf "\n\n">>$path/device_$device_name.txt

