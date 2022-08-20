#!/bin/bash

utcs_dir="/etc/utcs/scripts"

local_product_name=`sudo cat /sys/class/dmi/id/product_name`
local_pcid=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'`
pcid_left=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'|awk -F : '{print $(NF-1)}'`
pcid_right=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'|awk -F : '{print $NF}'` 
vendor_name=`sudo lscpu |grep 'Vendor ID'|awk '{print $NF}'`
sources_list=`sudo cat /etc/apt/sources.list`

lst_pcid=(0082 0083 0084 0085 0087 0089 008A 008B 0090 0091 02F0 06F0 0885 0886 0887 0888 088E 088F 0890 0891 0892 0893 0894 0895 0896 0897 08AE 08AF 08B1 08B2 08B3 08B4 095A 095B 24F3 24F4 24F5 24F6 24FB 24FD 2526 271B 271C 2720 2723 2725 30DC 3165 3166 31DC 34F0 3DF0 422B 422C 4232 4235 4236 4237 4238 4239 423A 423B 423C 423D 43F0 7A70 7AF0 9DF0 A0F0 A370 7200)
lst_type=(utcs_tool iwlwifi-driver)


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
    echo -e "#######################################执行$1安装开始#######################################"
}

fun_end()
{
    echo -e "#######################################执行$1安装结束#######################################"
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
    sudo apt remove --purge deepin-nvidia-installer utcs -y
    sudo apt remove --purge backport-iwlwifi-dkms -y
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

fix_iwlwifi-driver()
{
    fun_start ${lst_type[1]}
    
    sed -i "/lspci -n/s/0082/$pcid_right/g" $utcs_dir/fix_wifi.sh
    sed -i "/lspci -n/s/8086/$pcid_left/g" $utcs_dir/fix_wifi.sh
    sed -i "/if lspci -n/s/095A/3333/g" $utcs_dir/fix_wifi.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_wifi.sh |grep lspci
    #检查物理pcid修改情况
    echo -e "\n"

    echo -e "\nnvidia-driver依赖包检查..."
    sudo dpkg --get-selections | grep backport-iwlwifi-dkms
    echo -e "\nnvidia-driver依赖包删除..."
    sudo apt remove --purge backport-iwlwifi-dkms -y
    echo -e "\nnvidia-driver依赖包删除后检查..."
    sudo dpkg --get-selections | grep backport-iwlwifi-dkms
    echo -e "\n"
    
    utcs_run    
    echo -e "\n"
	
    echo -e "配置文件检查..."
    sudo dpkg --get-selections | grep backport-iwlwifi-dkms
    echo -e "\n"
    echo -e "配置文件删除..."

    sed -i "/lspci -n/s/$pcid_right/0082/g" $utcs_dir/fix_wifi.sh
    sed -i "/lspci -n/s/$pcid_left/8086/g" $utcs_dir/fix_wifi.sh	
    sed -i "/if lspci -n/s/3333/095A/g" $utcs_dir/fix_wifi.sh
    #还原逻辑pcid
    cat $utcs_dir/fix_wifi.sh |grep lspci
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    
    fun_end ${lst_type[1]}
}


main_menu()
{
    device_info
    utcs_init
    fix_iwlwifi-driver
    echo -e "\n\n"
}

main_menu
