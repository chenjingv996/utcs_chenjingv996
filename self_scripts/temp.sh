#!/usr/bin/env python
#coding:utf-8

self_path = "/home/chenjing/utcs_chenjingv996/"
py_info = `ls -l *.py`
sh_info = `ls -l *.sh`

fn_start()
{
    echo "\n"
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
    cd ${self_path}/self_scripts	
    echo -e "python脚本为:\n${py_info}\n"
    echo -e "\n"
    echo -e "shell脚本为:\n${sh_info}\n"
    echo -e "该文件夹下共有$(${py_info}|wc -l)个python脚本，$(${sh_info}|wc -l)个shell脚本"
    fn_stop
}

main_menu()
{
    echo -e "当前时间为:"$(date "+%Y-%m-%d %H:%M:%S")
    scripts_total
    echo -e "\n\n"
}


main_menu


