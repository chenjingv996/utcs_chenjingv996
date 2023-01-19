#!/bin/bash

####log_correct函数打印正确的输出到日志文件

function log_correct () 
{
DATE=`date "+%Y-%m-%d %H:%M:%S"` ####显示打印日志的时间
USER=$(whoami) ####那个用户在操作
echo "${DATE} ${USER} execute $0 [INFO] $@" >> ./successLog.log  
#####（$0脚本本身，$@将参数作为整体传输调用, >>将输出结果以追加的方式添加重定向到本地文件中(地址采用绝对路径)）
}


function log_error ()
{
DATE=`date "+%Y-%m-%d %H:%M:%S"`
USER=$(whoami)
echo "${DATE} ${USER} execute $1 [ERROR] $@" >> ./errorLog.log
}

if [ $# -eq 2 ];
then
    log_correct "执行的开始日期为: ${startDate} 结束日期为: ${endDate}"
else
    log_error "请输入执行的开始时间和结束时间，输入的两个日期参数格式必须是yyyy-MM-dd"
fi

