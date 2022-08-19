#!/bin/bash

current_time=$(date "+%Y-%m-%d %H:%M:%S")
utcs_dir="/etc/utcs/scripts"
utcs_tool="/home/uos/utcs_1.0-1_all.deb"
local_product_name=`sudo cat /sys/class/dmi/id/product_name`
local_pcid=`sudo lspci -nn |grep -i net|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'`
pcid_left=`sudo lspci -nn |grep -i usb|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'|awk -F : '{print $(NF-1)}'`
pcid_right=`sudo lspci -nn |grep -i usb|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'|awk -F : '{print $NF}'` 
devices_info=`sudo cat  /etc/utcs/scripts/fix_ethernet.sh |grep true|grep ^fix`
vendor_name=`sudo lscpu |grep 'Vendor ID'|awk '{print $NF}'`
vga_left=`sudo lspci -n | grep -i '0300:'|sed -n '1p'|awk '{print $3}'|awk -F ':' '{print $1}'`


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
    echo -e "##############################utcs环境初始化#################################"
    sleep 1 
    echo -e "utcs环境恢复开始..."
    sudo dpkg -P utcs 
    sudo dpkg -i $utcs_tool
    sudo dpkg -l |grep utcs
    sleep 2
    echo -e "\n"
    echo -e "utcs环境恢复完成..." 
    sudo apt remove nvidia-driver* backport-iwlwifi-dkms
    # 卸载已安装驱动
    echo -e "\n\n"
    sudo apt list | egrep  'nvidia-driver|backport-iwlwifi-dkms'
    # 检查已安装驱动卸载情况
    echo -e "\n\n"
    sed -i "/if lspci -n/s/095A/3333/g" $utcs_dir/fix_wifi.sh
    # 修改物理pcid为逻辑pcid
    echo -e "\n\n"
    cat $utcs_dir/fix_wifi.sh | egrep '3333'
    # 检查逻辑pcid修改情况
    echo -e "\n\n"
    

    echo -e "###############################################################ethernet11111111111"
    sleep 1 
    echo -e "fix_productname_n551zu测试开始"
    sed -i "/exists/s/N551ZU/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑product_name为物理product_name
    echo -e "\n\n"
    cat $utcs_dir/fix_ethernet.sh |grep exists|grep "$local_product_name"
    #检查逻辑product_name修改情况
    echo -e "\n\n"
    

    echo -e "###############################################################video66666666"
    sleep 1 
    echo -e "fix_video_666666测试开始"   
    sed -i "/if lspci -n/s/10de/$vga_left/g" $utcs_dir/fix_video.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_video.sh |grep lspci
    #检查逻辑pcid修改情况
    echo -e "\n\n"
    
    echo -e "###############################################################wifiwifiwifi3333333"
    sleep 1 
    echo -e "fix_pci_wifi3333333333333333333333333测试开始"
    sed -i "/lspci -n/s/0082/$pcid_right/g" $utcs_dir/fix_wifi.sh
    sed -i "/lspci -n/s/8086/$pcid_left/g" $utcs_dir/fix_wifi.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_wifi.sh |grep lspci
    #检查逻辑pcid修改情况
    echo -e "utcs执行开始..."
    echo -e "@@@@@@@@@@@@@@@@@@@@@start时间为:"$current_time
    sudo utcs
    #同时多设备多策略执行utcs
    echo -e "@@@@@@@@@@@@@@@@@@@@@middle时间为:"$current_time
    echo -e "配置文件检查..."
    echo -e "@@@@@@@@@@@@@@@@@@@@@end时间为:"$current_time


    echo -e "#############################配置文件清除123456789##################################"
    echo -e "配置文件检查..."
    cat /etc/modprobe.d/asus_nb_wmi.conf
    #检查配置文件的写入情况
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/asus_nb_wmi.conf
    #删除配置文件
    cat /etc/modprobe.d/asus_nb_wmi.conf
    #检查配置文件删除情况
    echo -e "\n\n" 

    sed -i "/exists/s/$local_product_name/N551ZU/g" $utcs_dir/fix_ethernet.sh    
    #还原逻辑product_name
    cat $utcs_dir/fix_ethernet.sh|grep exists|grep N551ZU
    #检查逻辑product_name还原情况
    echo -e "\n\n"
    sleep 2
    echo -e "fix_productname_n551zu测试完成"
    

    sed -i "/if lspci -n/s/$vga_left/10de/g" $utcs_dir/fix_video.sh
    sed -i "/if lspci -n/s/3333/095A/g" $utcs_dir/fix_wifi.sh  
    #还原逻辑pcid  
    cat $utcs_dir/fix_video.sh |grep lspci
    #检查逻辑pcid还原情况
    echo -e "\n\n" 
    sleep 2
    echo -e "fix_video_666666测试完成"	


    sed -i "/lspci -n/s/$pcid_right/0082/g" $utcs_dir/fix_wifi.sh
    sed -i "/lspci -n/s/$pcid_left/8086/g" $utcs_dir/fix_wifi.sh	
    #还原逻辑pcid  
    cat $utcs_dir/fix_wifi.sh |grep lspci
    #检查逻辑pcid还原情况
    echo -e "\n\n"
    sudo apt list | egrep  'nvidia-driver|backport-iwlwifi-dkms' 
    #检查脚本驱动安装情况 
    echo -e "\n\n"
    sed -i "/if lspci -n/s/3333/095A/g" $utcs_dir/fix_wifi.sh
    #还原逻辑pcid
    echo -e "\n\n"
    sleep 2
    echo -e "fix_pci_rtl8852ae测试完成"


    echo -e "*********************所有utcs脚本测试执行完成*********************"   
else
    echo -e "不存在该目录！"
fi
echo -e "\n\n"
