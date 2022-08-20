#!/bin/bash

current_time=$(date "+%Y-%m-%d %H:%M:%S")
utcs_dir="/etc/utcs/scripts"
utcs_tool="/home/uos/utcs_1.0-1_all.deb"
local_product_name=`sudo cat /sys/class/dmi/id/product_name`
local_pcid=`sudo lspci -nn |grep -i net|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'`
vga_pcid=`sudo lspci -n | grep -i '0300:'|sed -n '1p'`
vga_left=`sudo lspci -n | grep -i '0300:'|sed -n '1p'|awk '{print $3}'|awk -F ':' '{print $1}'`
devices_info=`sudo cat  /etc/utcs/scripts/fix_ethernet.sh |grep true|grep ^fix`
vendor_name=`sudo lscpu |grep 'Vendor ID'|awk '{print $NF}'`
#video_index=`lspci -n | grep -i 8086 | egrep -i '.*03(80|0[0-2])'`

echo -e "当前时间为:"$current_time
echo -e "\n"
echo -e "当前设备VERSION为:"`uname -a`
echo -e "当前设备VENDOR为:"$vendor_name
echo -e "当前脚本PATH为:"$utcs_dir
echo -e "当前设备NAME为:"$local_product_name
echo -e "当前设备PCID为:"$local_pcid
echo -e "已支持设备列表为:"$devices_info
echo -e "\n"

if [ -d "$utcs_dir" -a -f "$utcs_tool" ] 
then
    echo -e "*********************所有utcs脚本测试执行开始*********************"
    # sleep 1 
    # echo -e "fix_productname_x550vc测试开始"
    # sed -i "/exists/s/X550VC/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    # echo -e "utcs执行开始..."
    # sudo utcs
    # echo -e "配置文件检查..."
    # cat /etc/utcs/scripts/fix_ethernet.sh | grep -A2 "fix_productname_x550vc"
    # echo -e "\n"

    # cat /etc/modprobe.d/asus_nb_wmi.conf
    # echo -e "配置文件删除..."
    # rm /etc/modprobe.d/asus_nb_wmi.conf  	
    # sed -i "/exists/s/$local_product_name/X550VC/g" $utcs_dir/fix_ethernet.sh  
    # sleep 2
    # echo -e "fix_productname_x550vc测试完成"
    # echo -e "\n\n"
    
   
    echo -e "##############################utcs环境初始化#################################"
    sleep 1 
    echo -e "utcs环境恢复开始..."
    sudo dpkg -P utcs 
    sudo dpkg -i $utcs_tool
    sudo dpkg -l |grep utcs
    sleep 2
    echo -e "\n"
    echo -e "utcs环境恢复完成..." 
    sed -i "/if lspci -n/s/095A/3333/g" $utcs_dir/fix_wifi.sh
    echo -e "\n\n"

    echo -e "###############################################################video66666666"
    sleep 1 
    echo -e "fix_video_666666测试开始"
   
    sed -i "/if lspci -n/s/10de/$vga_left/g" $utcs_dir/fix_video.sh

    cat $utcs_dir/fix_video.sh |grep lspci
    echo -e "T1:$current_time"
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "T2:$current_time"
    echo -e "配置文件检查..."
    echo -e "\n"
   
    echo -e "配置文件删除..."

    sed -i "/if lspci -n/s/$vga_left/10de/g" $utcs_dir/fix_video.sh
    sed -i "/if lspci -n/s/3333/095A/g" $utcs_dir/fix_wifi.sh    

    cat $utcs_dir/fix_video.sh |grep lspci
      
    sleep 2
    echo -e "fix_video_666666测试完成"	
    echo -e "\n\n"



    echo -e "*********************所有utcs脚本测试执行完成*********************"   
else
    echo -e "不存在该目录！"
fi
echo -e "\n\n"
