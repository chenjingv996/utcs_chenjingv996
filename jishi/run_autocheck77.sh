#!/bin/bash

chmod a+x *.py *.sh
if [ -f "./run_local_console_logfile.log" ];then
echo -e "\nwarning:the logfile is exist,delete it!\n"
rm run_local_console_logfile.log &&  ./demo_local77_logfile.py 
sleep 2
echo -e "`seq -s '-' 80|sed s/[0-9]//g`\n"
cat run_local_console_logfile.log

else
echo -e "\nwarning:the logfile is not exist,create it!\n"
./demo_local77_logfile.py	
sleep 2
echo -e "`seq -s '-' 80|sed s/[0-9]//g`\n"
cat run_local_console_logfile.log

fi
