#!/bin/bash

current_time=`date +%F\%T`
utcs_dir="/etc/utcs/scripts"
utcs_tool="/home/uos/utcs_1.0-1_all.deb"
local_product_name=`sudo cat /sys/class/dmi/id/product_name`
local_pcid=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'`
pcid_left=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'|awk -F : '{print $(NF-1)}'`
pcid_right=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'|awk -F : '{print $NF}'` 
devices_info=`sudo cat  /etc/utcs/scripts/fix_ethernet.sh |grep true|grep ^fix`
vendor_name=`sudo lscpu |grep 'Vendor ID'|awk '{print $NF}'`


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
    
   
    # echo -e "###############################################################"
    # sleep 1 
    # echo -e "fix_pci_rtl8852ae测试开始"

    # sed -i "/exists/s/10ec:8852/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    # echo -e "utcs执行开始..."
    # sudo utcs
    # echo -e "配置文件检查..."
    # cat /etc/utcs/scripts/fix_ethernet.sh | grep -A2 "fix_pci_rtl8852ae"
    # echo -e "\n"

    # echo -e "配置文件删除..."

    # sed -i "/exists/s/$local_pcid/10ec:8852/g" $utcs_dir/fix_ethernet.sh    
    # sleep 2
    # echo -e "fix_pci_rtl8852ae测试完成"	
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

    echo -e "###############################################################wifiwifiwifi3333333"
    sleep 1 
    echo -e "fix_pci_wifi3333333333333333333333333测试开始"

    sed -i "/lspci -n/s/0082/$pcid_right/g" $utcs_dir/fix_wifi.sh
    sed -i "/lspci -n/s/8086/$pcid_left/g" $utcs_dir/fix_wifi.sh

    cat $utcs_dir/fix_wifi.sh |grep lspci

    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."
    cat /etc/utcs/scripts/fix_ethernet.sh | grep -A2 "fix_pci_rtl8852ae"
    echo -e "\n"

    echo -e "配置文件删除..."

    sed -i "/lspci -n/s/$pcid_right/0082/g" $utcs_dir/fix_wifi.sh
    sed -i "/lspci -n/s/$pcid_left/8086/g" $utcs_dir/fix_wifi.sh	

    cat $utcs_dir/fix_wifi.sh |grep lspci
      
    sleep 2
    echo -e "fix_pci_rtl8852ae测试完成"	
    sed -i "/if lspci -n/s/3333/095A/g" $utcs_dir/fix_wifi.sh
    echo -e "\n\n"



    echo -e "*********************所有utcs脚本测试执行完成*********************"   
else
    echo -e "不存在该目录！"
fi
echo -e "\n\n"
