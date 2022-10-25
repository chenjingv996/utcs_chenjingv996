#!/bin/bash

echo -e "######################################################\n"

curr_time=`date +%F\ %H:%M:%S`

echo -e "${curr_time}\n"

echo -e "$(date +%F_%T)\n"

for i in `seq 9`
do
    for j in `seq $i 9`
    do
	    echo -n "$i*$j=$(($i*$j))  "
    done
    echo
done
echo


echo -e "\n"
