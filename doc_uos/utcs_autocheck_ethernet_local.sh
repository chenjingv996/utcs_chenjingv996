#!/bin/bash

current_time=$(date "+%Y-%m-%d %H:%M:%S")
utcs_dir="/etc/utcs/scripts"
utcs_tool="/home/uos/utcs_1.0-1_all.deb"
local_product_name=`sudo cat /sys/class/dmi/id/product_name`
local_pcid=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'`
pcid_left=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'|awk -F ':' '{print $(NF-1)}'`
pcid_right=`sudo lspci -nn |grep -i vga|awk -F '[' '{print $NF}'|awk -F ']' '{print $1}'|sed -n '1p'|awk -F ':' '{print $NF}'`

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
	
    echo -e "*********************所有utcs脚本测试执行开始*********************"
    sleep 1 
    echo -e "fix_productname_x550vc测试开始"
    sed -i "/exists/s/X550VC/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/asus_nb_wmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/asus_nb_wmi.conf  	
    sed -i "/exists/s/$local_product_name/X550VC/g" $utcs_dir/fix_ethernet.sh  
    sleep 2
    echo -e "fix_productname_x550vc测试完成"
    echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_productname_n551zu测试开始"
    sed -i "/exists/s/N551ZU/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/asus_nb_wmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/asus_nb_wmi.conf
    sed -i "/exists/s/$local_product_name/N551ZU/g" $utcs_dir/fix_ethernet.sh    
    sleep 2
    echo -e "fix_productname_n551zu测试完成"
    echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_xiaomi_notebook_133测试开始"
    sed -i "/exists/s/TM1613/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/8086:24f3/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/xiaomi_disable_acer_wmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/xiaomi_disable_acer_wmi.conf
    sed -i "/exists/s/$local_product_name/TM1613/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/8086:24f3/g" $utcs_dir/fix_ethernet.sh      
    sleep 2
    echo -e "fix_xiaomi_notebook_133测试完成"
    echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_lenovo_y700测试开始"
    sed -i "/exists/s/80NV/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/8086:3166/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/ideapad.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/ideapad.conf  	
    sed -i "/exists/s/$local_product_name/80NV/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/8086:3166/g" $utcs_dir/fix_ethernet.sh    
    sleep 2
    echo -e "fix_lenovo_y700测试完成"
    echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_lenovo_r720测试开始"
    sed -i "/exists/s/80WW/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/168c:0042/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."
 
    echo -e "\n"

    cat /etc/modprobe.d/ideapad.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/ideapad.conf  
    sed -i "/exists/s/$local_product_name/80WW/g" $utcs_dir/fix_ethernet.sh
    sed -i "/exists/s/$local_pcid/168c:0042/g" $utcs_dir/fix_ethernet.sh    
    sleep 2
    echo -e "fix_lenovo_r720测试完成"
    echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_asus_x450jb测试开始"
    sed -i "/exists/s/X450JB/$local_product_name/g" $utcs_dir/fix_ethernet.sh

    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/blacklist_acerwmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/blacklist_acerwmi.conf
    sed -i "/exists/s/$local_product_name/X450JB/g" $utcs_dir/fix_ethernet.sh
  
    sleep 2
    echo -e "fix_asus_x450jb测试完成"
    echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_asus_x450jn测试开始"
    sed -i "/exists/s/X450JN/$local_product_name/g" $utcs_dir/fix_ethernet.sh
 
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/blacklist_acerwmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/blacklist_acerwmi.conf  
    sed -i "/exists/s/$local_product_name/X450JN/g" $utcs_dir/fix_ethernet.sh
  
    sleep 2
    echo -e "fix_asus_x450jn测试完成"
    echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_asus_x450jf测试开始"
    sed -i "/exists/s/X450JF/$local_product_name/g" $utcs_dir/fix_ethernet.sh

    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/blacklist_acerwmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/blacklist_acerwmi.conf  
    sed -i "/exists/s/$local_product_name/X450JF/g" $utcs_dir/fix_ethernet.sh
  
    sleep 2
    echo -e "fix_asus_x450jf测试完成"
    echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_asus_u82u测试开始"
    sed -i "/exists/s/U82U/$local_product_name/g" $utcs_dir/fix_ethernet.sh

    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/blacklist_asus_nb_wmi.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/blacklist_asus_nb_wmi.conf  
    sed -i "/exists/s/$local_product_name/U82U/g" $utcs_dir/fix_ethernet.sh
 
    sleep 2
    echo -e "fix_asus_u82u测试完成"
    echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_lenovo_80t9测试开始"
    sed -i "/exists/s/80T9/$local_product_name/g" $utcs_dir/fix_ethernet.sh

    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/blacklist-ideapad-laptop.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/blacklist-ideapad-laptop.conf  
    sed -i "/exists/s/$local_product_name/80T9/g" $utcs_dir/fix_ethernet.sh
 
    sleep 2
    echo -e "fix_lenovo_80t9测试完成"
    echo -e "\n\n"

    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_pci_bcm4313测试开始"

    sed -i "/exists/s/14e4:4727/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/bcm.conf
    cat /etc/modules
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/bcm.conf
    sed -i "/brcmsmac/"d /etc/modules

    sed -i "/exists/s/$local_pcid/14e4:4727/g" $utcs_dir/fix_ethernet.sh    
    sleep 2
    echo -e "fix_pci_bcm4313测试完成"	
    echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_pci_bcm4350测试开始"

    sed -i "/exists/s/14e4:43a3/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/bcm.conf
    echo -e "配置文件删除..."

    echo -e "\n"

    rm /etc/modprobe.d/bcm.conf 

    sed -i "/exists/s/$local_pcid/14e4:43a3/g" $utcs_dir/fix_ethernet.sh    
    sleep 2
    echo -e "fix_pci_bcm4350测试完成"	
    echo -e "\n\n"

    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_pci_bcm4356测试开始"

    sed -i "/exists/s/17aa:0777/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."
   
    echo -e "\n"

    #cat /etc/modprobe.d/bcm.conf
    echo -e "配置文件删除..."
 
    echo -e "\n"

    #rm /etc/modprobe.d/bcm.conf 

    sed -i "/exists/s/$local_pcid/17aa:0777/g" $utcs_dir/fix_ethernet.sh    
    sleep 2
    echo -e "fix_pci_bcm4356测试完成"	
    echo -e "\n\n"

#    echo -e "###############################################################"
#    sleep 1 
#    echo -e "fix_pci_bcm4322测试开始"
#    
#    sed -i "/exists/s/14e4:432b/$local_pcid/g" $utcs_dir/fix_ethernet.sh
#    echo -e "utcs执行开始..."
#    sudo utcs
#    echo -e "配置文件检查..."
#
#    echo -e "\n"
#
#    cat /etc/modprobe.d/bcm.conf
#    echo -e "配置文件删除..."
#    rm /etc/modprobe.d/bcm.conf 
#    
#    sed -i "/exists/s/$local_pcid/14e4:432b/g" $utcs_dir/fix_ethernet.sh    
#    sleep 2
#    echo -e "fix_pci_bcm4322测试完成"	
#    echo -e "\n\n"

    # echo -e "###############################################################"
    # sleep 1 
    # echo -e "fix_pci_ar9485_nohwcrypt测试开始"
    # # sed -i "/exists/s/80WW/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    # sed -i "/exists/s/168C:0032/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    # echo -e "utcs执行开始..."
    # sudo utcs
    # echo -e "配置文件检查..."

    # echo -e "\n"

    # cat /etc/modprobe.d/ath9k.conf
    # echo -e "配置文件删除..."
    # rm /etc/modprobe.d/ath9k.conf 
    # # sed -i "/exists/s/$local_product_name/80WW/g" $utcs_dir/fix_ethernet.sh
    # sed -i "/exists/s/$local_pcid/168C:0032/g" $utcs_dir/fix_ethernet.sh    
    # sleep 2
    # echo -e "fix_pci_ar9485_nohwcrypt测试完成"	
    # echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_pci_rtl8723be_fwlps测试开始"

    sed -i "/exists/s/10ec:b723/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."
 
    echo -e "\n"

    cat /etc/modprobe.d/rtl8723be.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/rtl8723be.conf 

    sed -i "/exists/s/$local_pcid/10ec:b723/g" $utcs_dir/fix_ethernet.sh    
    sleep 2
    echo -e "fix_pci_rtl8723be_fwlps测试完成"	
    echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_pci_rtl8188ce测试开始"

    sed -i "/exists/s/10ec:8176/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/rtl8192ce.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/rtl8192ce.conf 

    sed -i "/exists/s/$local_pcid/10ec:8176/g" $utcs_dir/fix_ethernet.sh    
    sleep 2
    echo -e "fix_pci_rtl8188ce测试完成"	
    echo -e "\n\n"
    
    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_pci_rt3290测试开始"

    sed -i "/exists/s/1814:3290/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."
 
    echo -e "\n"

    cat /etc/modprobe.d/rt2800pci.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/rt2800pci.conf 

    sed -i "/exists/s/$local_pcid/1814:3290/g" $utcs_dir/fix_ethernet.sh    
    sleep 2
    echo -e "fix_pci_rt3290测试完成"	
    echo -e "\n\n"
    
    # echo -e "###############################################################"
    # sleep 1 
    # echo -e "fix_usb_rtl8723au测试开始"
    # # sed -i "/exists/s/80WW/$local_product_name/g" $utcs_dir/fix_ethernet.sh
    # sed -i "/exists/s/0bda:1724/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    # echo -e "utcs执行开始..."
    # sudo utcs
    # echo -e "配置文件检查..."

    #echo -e "\n"

    # cat /etc/modprobe.d/rt2800pci.conf
    # echo -e "配置文件删除..."
    # rm /etc/modprobe.d/rt2800pci.conf 
    # sed -i "/exists/s/$local_product_name/80WW/g" $utcs_dir/fix_ethernet.sh
    # sed -i "/exists/s/$local_pcid/0bda:1724/g" $utcs_dir/fix_ethernet.sh    
    # sleep 2
    # echo -e "fix_usb_rtl8723au测试完成"	
    # echo -e "\n\n"

    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_pci_rtl8723ae_fwlps测试开始"

    sed -i "/exists/s/10ec:8723/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    cat /etc/modprobe.d/rtl8723ae.conf
    echo -e "配置文件删除..."
    rm /etc/modprobe.d/rtl8723ae.conf 

    sed -i "/exists/s/$local_pcid/10ec:8723/g" $utcs_dir/fix_ethernet.sh    
    sleep 2
    echo -e "fix_pci_rtl8723ae_fwlps测试完成"	
    echo -e "\n\n"

    echo -e "###############################################################"
    sleep 1 
    echo -e "fix_pci_rtl8852ae测试开始"

    sed -i "/exists/s/10ec:8852/$local_pcid/g" $utcs_dir/fix_ethernet.sh
    echo -e "utcs执行开始..."
    sudo utcs
    echo -e "配置文件检查..."

    echo -e "\n"

    echo -e "配置文件删除..."

    sed -i "/exists/s/$local_pcid/10ec:8852/g" $utcs_dir/fix_ethernet.sh    
    sleep 2
    echo -e "fix_pci_rtl8852ae测试完成"	
    sed -i "/if lspci -n/s/3333/095A/g" $utcs_dir/fix_wifi.sh
    echo -e "\n\n"

    echo -e "*********************所有utcs脚本测试执行完成*********************"   
else
    echo -e "不存在该目录！"
fi
echo -e "\n\n"
