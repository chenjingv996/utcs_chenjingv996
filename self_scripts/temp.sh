#!/bin/bash

self_path="/home/chenjing/utcs_chenjingv996/self_scripts"

py_info=`ls -l *.py`
sh_info=`ls -l *.sh`

fn_start()
{
    echo -e "\n"
    echo -e "########################计算开始####################################"
}

fn_stop()
{
    echo -e "\n"
    echo -e "########################计算结束####################################"
}

scripts_total()
{
    fn_start
    cd ${self_path}	
    echo -e "python脚本为:\n$py_info\n"
    echo -e "shell脚本为:\n$sh_info\n"
    echo -e "该文件夹下包括$(ls -l *.py|wc -l)个python脚本，$(ls -l *.sh|wc -l)个shell脚本!"
    fn_stop
}

main_menu()
{
    echo -e "当前时间为:"$(date "+%Y-%m-%d %H:%M:%S")
    scripts_total
    echo -e "\n\n"
}


main_menu


