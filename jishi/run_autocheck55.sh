#!/bin/bash

rm run_local_console_logfile.log &&  ./demo_local55_logfile.py     

echo -e "`seq -s '-' 80|sed s/[0-9]//g`\n"

cat run_local_console_logfile.log
