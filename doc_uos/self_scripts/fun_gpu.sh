#!/bin/bash

utcs_dir="/etc/utcs/scripts"

local_product_name=`sudo cat /sys/class/dmi/id/product_name`
local_pcid=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'`
vga_pcid=`sudo lspci -n | grep -i '0300:'|sed -n '1p'|awk '{print $3}'`
vga_left=`sudo lspci -n | grep -i '0300:'|sed -n '1p'|awk '{print $3}'|awk -F ':' '{print $1}'`
vga_right=`sudo lspci -n | grep -i '0300:'|sed -n '1p'|awk '{print $3}'|awk -F ':' '{print $2}'`
vendor_name=`sudo lscpu |grep 'Vendor ID'|awk '{print $NF}'`
sources_list=`sudo cat /etc/apt/sources.list`

lst_type=(utcs_tool is_innogpu_gpu fix_innogpu_gpudrv fix_nvidia_gpudrv fix_zhaoxin_6000 fix_zhaoxin_6000G) 

device_info()
{
    echo -e "#######################################获取当前设备信息#######################################"
    echo -e "当前时间为:"$(date "+%Y-%m-%d %H:%M:%S")
    echo -e "\n"
    echo -e "当前设备VERSION为:"$(uname -a)
    echo -e "当前设备VENDOR为:"$vendor_name
    echo -e "当前脚本PATH为:"$utcs_dir
    echo -e "当前设备NAME为:"$local_product_name
    echo -e "当前设备PCID为:"$local_pcid
    echo -e "当前设备仓库地址为:$sources_list"
    echo -e "\n"
}

fun_start()
{
    echo -e "\n"
    echo -e "#######################################执行$1脚本开始#######################################"
}

fun_end()
{
    echo -e "#######################################执行$1脚本结束#######################################"
    echo -e "\n"
}

utcs_run()
{
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "\n"
}

utcs_init()
{    
    echo -e "#######################################执行${lst_type[0]}初始化开始#######################################"   
    sleep 1 
    echo -e "utcs环境恢复开始..."
    echo -e "\n"
    sudo apt remove --purge deepin-nvidia-installer utcs firmware-brcm80211 -y
    sudo apt remove --purge zhaoxin-linux-graphics-driver-dri -y 
    sudo apt remove --purge cx4-linux-graphics-driver-dri -y
    #卸载utcs工具 
    sudo apt install utcs -y
    #安装utcs工具
    sudo dpkg --get-selections |egrep "deepin-nvidia-installer|utcs"
    #检查utcs工具安装情况
    sleep 1
    echo -e "\n"
    echo -e "utcs环境恢复完成..." 
    echo -e "\n"
    echo -e "#######################################执行${lst_type[0]}初始化结束#######################################" 
}

is_innogpu_gpu()
{
    sed -i "/local VID/s/1EC8/$vga_left/g" $utcs_dir/fix_gpu.sh
    sed -i "/local ID0/s/1EA8/$vga_right/g" $utcs_dir/fix_gpu.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_gpu.sh |grep "local VID" -A10
    #检查物理pcid修改情况
    echo -e "\n"
}

fix_innogpu_gpudrv()
{
    fun_start ${lst_type[2]}
   
    cnt=$(arch | grep -E "aarch64|x86_64|loongarch" | wc -l)
    if [ $cnt -eq 1 ]; then
        is_innogpu_gpu
    fi
    echo -e "\n"
    
    utcs_run

    sed -i "/local VID/s/$vga_left/1EC8/g" $utcs_dir/fix_gpu.sh
    sed -i "/local ID0/s/$vga_right/1EA8/g" $utcs_dir/fix_gpu.sh
    #还原逻辑pcid
    cat $utcs_dir/fix_gpu.sh |grep "local VID" -A10
    #检查逻辑pcid还原情况
    echo -e "\n"
   
    fun_end ${lst_type[2]}
}

fix_nvidia_gpudrv()
{
    fun_start ${lst_type[3]}

    sed -i "/if lspci -n/s/10de/$vga_left/g" $utcs_dir/fix_gpu.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_gpu.sh |grep lspci
    #检查物理pcid修改情况
    echo -e "\n"
    
    utcs_run
   
    sed -i "/if lspci -n/s/$vga_left/10de/g" $utcs_dir/fix_gpu.sh  
    #还原逻辑pcid
    cat $utcs_dir/fix_gpu.sh |grep lspci
    #检查逻辑pcid还原情况
    echo -e "\n"

    fun_end ${lst_type[3]}
}

fix_zhaoxin_6000()
{
    fun_start ${lst_type[4]}

    sed -i "/if lspci -n/s/1D17/$vga_left/g" $utcs_dir/fix_gpu.sh
    sed -i "/if lspci -n/s/3A03/$vga_right/g" $utcs_dir/fix_gpu.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_gpu.sh |grep lspci
    #检查物理pcid修改情况
    echo -e "\n"
    
    utcs_run
   
    sed -i "/if lspci -n/s/$vga_left/1D17/g" $utcs_dir/fix_gpu.sh
    sed -i "/if lspci -n/s/$vga_right/3A03/g" $utcs_dir/fix_gpu.sh  
    #还原逻辑pcid
    cat $utcs_dir/fix_gpu.sh |grep lspci
    #检查逻辑pcid还原情况
    echo -e "\n"

    fun_end ${lst_type[4]}
}

fix_zhaoxin_6000G()
{
    fun_start ${lst_type[5]}

    sed -i "/if lspci -n/s/1D17/$vga_left/g" $utcs_dir/fix_gpu.sh
    sed -i "/if lspci -n/s/3D01/$vga_right/g" $utcs_dir/fix_gpu.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_gpu.sh |grep lspci
    #检查物理pcid修改情况
    echo -e "\n"
    
    utcs_run
   
    sed -i "/if lspci -n/s/$vga_left/1D17/g" $utcs_dir/fix_gpu.sh
    sed -i "/if lspci -n/s/$vga_right/3D01/g" $utcs_dir/fix_gpu.sh  
    #还原逻辑pcid
    cat $utcs_dir/fix_gpu.sh |grep lspci
    #检查逻辑pcid还原情况
    echo -e "\n"

    fun_end ${lst_type[5]}
}


main_menu()
{
    device_info
    utcs_init
    fix_innogpu_gpudrv
    fix_nvidia_gpudrv
    fix_zhaoxin_6000
    fix_zhaoxin_6000G
    echo -e "\n\n"
}

main_menu
