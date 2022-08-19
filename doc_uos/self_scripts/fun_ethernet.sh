#!/bin/bash

utcs_dir="/etc/utcs/scripts"

local_product_name=`sudo cat /sys/class/dmi/id/product_name`
local_pcid=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'`
pcid_left=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'|awk -F ':' '{print $(NF-1)}'`
pcid_right=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'|awk -F ':' '{print $NF}'`
device_list=`sudo cat  /etc/utcs/scripts/fix_ethernet.sh |grep true|grep ^fix`
vendor_name=`sudo lscpu |grep 'Vendor ID'|awk '{print $NF}'`
sources_list=`sudo cat /etc/apt/sources.list`

lst_type=(utcs_tool fix_productname_x550vc fix_productname_n551zu fix_xiaomi_notebook_133 fix_lenovo_y700 fix_lenovo_r720 fix_asus_x450jb fix_asus_x450jn fix_asus_x450jf fix_asus_u82u fix_lenovo_80t9 fix_pci_bcm4313 fix_pci_bcm4350 fix_pci_bcm4356 fix_pci_rtl8723be_fwlps fix_pci_rtl8188ce fix_pci_rt3290 fix_pci_rtl8723ae_fwlps fix_pci_rtl8852ae)
lst_product_name=(utcs_tool X550VC N551ZU TM1613 80NV 80WW X450JB X450JN X450JF U82U 80T9 QQQQ QQQQ QQQQ QQQQ QQQQ QQQQ QQQQ N70Z)
lst_pcid=(utcs:utcs q:q q:q 8086:24f3 8086:3166 168c:0042 q:q q:q q:q q:q q:q 14e4:4727 14e4:43a3 17aa:0777 10ec:b723 10ec:8176 1814:3290 10ec:8723 10ec:8852)

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
    sudo apt remove --purge deepin-nvidia-installer utcs -y
    sudo apt remove --purge firmware-brcm80211 rtl8852ae-dkms -y
    #卸载utcs工具 
    sudo apt install utcs -y
    sudo apt install bcmwl-kernel-source -y
    #安装utcs工具
    sudo dpkg --get-selections |egrep "deepin-nvidia-installer|utcs|bcmwl-kernel-source"
    #检查utcs工具安装情况
    sleep 1
    echo -e "\n"
    echo -e "utcs环境恢复完成..." 
    echo -e "\n"
    echo -e "#######################################执行${lst_type[0]}初始化结束#######################################" 
}

fix_productname_x550vc()
{    
    fun_start ${lst_type[1]}
    sleep 1 
    sed -i "/exists/s/${lst_product_name[1]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |grep "$local_product_name"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/asus_nb_wmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/asus_nb_wmi.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/asus_nb_wmi.conf
    echo -e "\n"

    sed -i "/exists/s/$local_product_name/${lst_product_name[1]}/g" $utcs_dir/fix_ethernet.sh  
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |grep "${lst_product_name[1]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[1]}
}

fix_productname_n551zu()
{   
    fun_start ${lst_type[2]}	
    sleep 1 
    sed -i "/exists/s/${lst_product_name[2]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |grep "$local_product_name"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/asus_nb_wmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/asus_nb_wmi.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/asus_nb_wmi.conf
    echo -e "\n"

    sed -i "/exists/s/$local_product_name/${lst_product_name[2]}/g" $utcs_dir/fix_ethernet.sh  
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |grep "${lst_product_name[2]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[2]}
}

fix_xiaomi_notebook_133()
{
    fun_start ${lst_type[3]}
    sleep 1 
    sed -i "/exists/s/${lst_product_name[3]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[3]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/xiaomi_disable_acer_wmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/xiaomi_disable_acer_wmi.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/xiaomi_disable_acer_wmi.conf
    echo -e "\n"

    sed -i "/exists/s/$local_product_name/${lst_product_name[3]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[3]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[3]}|${lst_pcid[3]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[3]}
}

fix_lenovo_y700()
{
    fun_start ${lst_type[4]}
    sleep 1 
    sed -i "/exists/s/${lst_product_name[4]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[4]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/ideapad.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/ideapad.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/ideapad.conf
    echo -e "\n"

    sed -i "/exists/s/$local_product_name/${lst_product_name[4]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[4]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[4]}|${lst_pcid[4]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[4]}
}

fix_lenovo_r720()
{
    fun_start ${lst_type[5]}
    sleep 1 
    sed -i "/exists/s/${lst_product_name[5]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[5]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/ideapad.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/ideapad.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/ideapad.conf
    echo -e "\n"

    sed -i "/exists/s/$local_product_name/${lst_product_name[5]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[5]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[5]}|${lst_pcid[5]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[5]}
}

fix_asus_x450jn()
{
    fun_start ${lst_type[6]}
    sleep 1 
    sed -i "/exists/s/${lst_product_name[6]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[6]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/blacklist_acerwmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/blacklist_acerwmi.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/blacklist_acerwmi.conf
    echo -e "\n"

    sed -i "/exists/s/$local_product_name/${lst_product_name[6]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[6]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[6]}|${lst_pcid[6]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[6]}
}

fix_asus_x450jb()
{
    fun_start ${lst_type[7]}
    sleep 1 
    sed -i "/exists/s/${lst_product_name[7]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    # sed -i "/exists/s/${lst_pcid[7]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/blacklist_acerwmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/blacklist_acerwmi.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/blacklist_acerwmi.conf
    echo -e "\n"

    sed -i "/exists/s/$local_product_name/${lst_product_name[7]}/g" $utcs_dir/fix_ethernet.sh
    # sed -i "/exists/s/$local_pcid/${lst_pcid[7]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[7]}|${lst_pcid[7]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[7]}
}

fix_asus_x450jf()
{
    fun_start ${lst_type[8]}
    sleep 1 
    sed -i "/exists/s/${lst_product_name[8]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[8]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

#     echo -e "配置文件检查..."
#     cat /etc/modprobe.d/blacklist_acerwmi.conf
#     echo -e "配置文件删除..."
#     rm /etc/modprobe.d/blacklist_acerwmi.conf
#     echo -e "配置文件删除后检查..."
#     cat /etc/modprobe.d/blacklist_acerwmi.conf
    echo -e "\n"

    sed -i "/exists/s/$local_product_name/${lst_product_name[8]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[8]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[8]}|${lst_pcid[8]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[8]}
}

fix_asus_u82u()
{
    fun_start ${lst_type[9]}
    sleep 1 
    sed -i "/exists/s/${lst_product_name[9]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    # sed -i "/exists/s/${lst_pcid[9]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/blacklist_asus_nb_wmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/blacklist_asus_nb_wmi.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/blacklist_asus_nb_wmi.conf
    echo -e "\n"

    sed -i "/exists/s/$local_product_name/${lst_product_name[9]}/g" $utcs_dir/fix_ethernet.sh
    # sed -i "/exists/s/$local_pcid/${lst_pcid[9]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[9]}|${lst_pcid[9]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[9]}
}

fix_lenovo_80t9()
{
    fun_start ${lst_type[10]}
    sleep 1 
    sed -i "/exists/s/${lst_product_name[10]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    # sed -i "/exists/s/${lst_pcid[10]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/blacklist-ideapad-laptop.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/blacklist-ideapad-laptop.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/blacklist-ideapad-laptop.conf
    echo -e "\n"

    sed -i "/exists/s/$local_product_name/${lst_product_name[10]}/g" $utcs_dir/fix_ethernet.sh
    # sed -i "/exists/s/$local_pcid/${lst_pcid[10]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[10]}|${lst_pcid[10]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[10]}
}

fix_pci_bcm4313()
{
    fun_start ${lst_type[11]}
    sleep 1 
    # sed -i "/exists/s/${lst_product_name[11]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[11]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/bcm.conf
    sudo apt list | egrep "firmware-brcm80211|bcmwl-kernel-source"
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/bcm.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/bcm.conf
    echo -e "\n"

    # sed -i "/exists/s/$local_product_name/${lst_product_name[11]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[11]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[11]}|${lst_pcid[11]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[11]}
}

fix_pci_bcm4350()
{
    fun_start ${lst_type[12]}
    sleep 1 
    # sed -i "/exists/s/${lst_product_name[12]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[12]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/bcm.conf
    sudo apt list | egrep "firmware-brcm80211|bcmwl-kernel-source"
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/bcm.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/bcm.conf
    echo -e "\n"

    # sed -i "/exists/s/$local_product_name/${lst_product_name[12]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[12]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[12]}|${lst_pcid[12]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[12]}
}

fix_pci_bcm4356()
{
    fun_start ${lst_type[13]}
    sleep 1 
    # sed -i "/exists/s/${lst_product_name[13]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[13]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
#     cat /etc/modprobe.d/bcm.conf
    sudo apt list | egrep "firmware-brcm80211|bcmwl-kernel-source"
#     echo -e "配置文件删除..."
#     rm /etc/modprobe.d/bcm.conf
#     echo -e "配置文件删除后检查..."
#     cat /etc/modprobe.d/bcm.conf
    echo -e "\n"

    # sed -i "/exists/s/$local_product_name/${lst_product_name[13]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[13]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[13]}|${lst_pcid[13]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[13]}
}

fix_pci_rtl8723be_fwlps()
{
    fun_start ${lst_type[14]}
    sleep 1 
    # sed -i "/exists/s/${lst_product_name[14]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[14]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/rtl8723be.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/rtl8723be.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/rtl8723be.conf
    echo -e "\n"

    # sed -i "/exists/s/$local_product_name/${lst_product_name[14]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[14]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[14]}|${lst_pcid[14]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[14]}
}

fix_pci_rtl8188ce()
{
    fun_start ${lst_type[15]}
    sleep 1 
    # sed -i "/exists/s/${lst_product_name[15]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[15]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/rtl8192ce.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/rtl8192ce.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/rtl8192ce.conf
    echo -e "\n"

    # sed -i "/exists/s/$local_product_name/${lst_product_name[15]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[15]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[15]}|${lst_pcid[15]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[15]}
}

fix_pci_rt3290()
{
    fun_start ${lst_type[16]}
    sleep 1 
    # sed -i "/exists/s/${lst_product_name[16]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[16]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/rt2800pci.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/rt2800pci.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/rt2800pci.conf
    echo -e "\n"

    # sed -i "/exists/s/$local_product_name/${lst_product_name[16]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[16]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[16]}|${lst_pcid[16]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[16]}
}

fix_pci_rtl8723ae_fwlps()
{
    fun_start ${lst_type[17]}
    sleep 1 
    # sed -i "/exists/s/${lst_product_name[17]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[17]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
    cat /etc/modprobe.d/rtl8723ae.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/rtl8723ae.conf
    echo -e "配置文件删除后检查..."
    cat /etc/modprobe.d/rtl8723ae.conf
    echo -e "\n"

    # sed -i "/exists/s/$local_product_name/${lst_product_name[17]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[17]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[17]}|${lst_pcid[17]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[17]}
}

fix_pci_rtl8852ae()
{
    fun_start ${lst_type[18]}
    sleep 1 
    sed -i "/exists/s/${lst_product_name[18]}/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/${lst_pcid[18]}/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    #修改逻辑pcid为物理pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "$local_product_name|$local_pcid"
    #检查物理pcid修改情况
    echo -e "\n"

    utcs_run

    echo -e "配置文件检查..."
#     cat /etc/modprobe.d/rtl8192ce.conf
    sudo apt list | grep rtl8852ae-dkms
#     echo -e "配置文件删除..."
#     rm /etc/modprobe.d/rtl8192ce.conf
#     echo -e "配置文件删除后检查..."
#     cat /etc/modprobe.d/rtl8192ce.conf
    echo -e "\n"

    sed -i "/exists/s/$local_product_name/${lst_product_name[18]}/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/${lst_pcid[18]}/g" $utcs_dir/fix_ethernet.sh   
    #还原逻辑pcid
    cat $utcs_dir/fix_ethernet.sh |egrep "${lst_product_name[18]}|${lst_pcid[18]}"
    #检查逻辑pcid还原情况
    sleep 1
    echo -e "\n"
    fun_end ${lst_type[18]}
}


main_menu()
{
    device_info
    utcs_init
    echo -e "已支持设备列表为:\n$device_list\n"
    fix_productname_x550vc
    fix_productname_n551zu
    fix_xiaomi_notebook_133
    fix_lenovo_y700 
    fix_lenovo_r720 
    fix_asus_x450jn 
    fix_asus_x450jb 
    fix_asus_x450jf 
    fix_asus_u82u 
    fix_lenovo_80t9 
    fix_pci_bcm4313 
    fix_pci_bcm4350 
    fix_pci_bcm4356
    fix_pci_rtl8723be_fwlps
    fix_pci_rtl8188ce
    fix_pci_rt3290 
    fix_pci_rtl8723ae_fwlps 
    fix_pci_rtl8852ae
    echo -e "\n\n"
}

main_menu
