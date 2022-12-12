#!/bin/bash

curr_time=`date +%F_%T`
self_path=`pwd`
py_info=`ls -l *.py`
sh_info=`ls -l *.sh`
py_count=`ls -l *.py|wc -l`
sh_count=`ls -l *.sh|wc -l`
total_count=`ls -l *.py *.sh|wc -l`
jing_count=`seq -s '#' 30|sed s/[0-9]//g`

fn_start()
{
    echo -e 
    echo -e "$jing_count测试执行开始$jing_count\n"
    echo -e 
}


fn_stop()
{
    echo -e 
    echo -e "$jing_count测试执行结束$jing_count\n"
    echo -e 
}

scripts_total()
{
    fn_start
    cd ${self_path}	
    echo -e "python脚本为:\n$py_info\n"
    echo -e "shell脚本为:\n$sh_info\n"
    echo -e "当前目录为:$self_path,该目录下共有$total_count个脚本文件,\n其中包含$py_count个python脚本，$sh_count个shell脚本!"
    fn_stop
}

main_menu()
{
    echo -e	
    echo -e "当前时间为:"$curr_time
    scripts_total
    echo -e 
}


main_menu


