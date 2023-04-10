#!/bin/bash

if [ -f "./run_office_console_logfile.log" ];then
echo -e "\nwarning:the logfile is exist,delete it!\n"
rm run_office_console_logfile.log &&  ./demo_office66_logfile.py     
sleep 2
echo -e "`seq -s '-' 80|sed s/[0-9]//g`\n"
cp run_office_console_logfile.log /home/test/autotest
cat run_office_console_logfile.log

else
echo -e "\nwarning:the logfile is not exist,create it!\n"
./demo_office66_logfile.py	
sleep 2
echo -e "`seq -s '-' 80|sed s/[0-9]//g`\n"
cat run_office_console_logfile.log

fi
