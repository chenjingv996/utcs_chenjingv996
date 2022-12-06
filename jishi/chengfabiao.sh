#!/bin/bash

echo
echo -e `date +%F_%T`
echo 

for i in `seq  9`
do
    for j in `seq  $i`       #这地方写成$i 就比写成seq 9 方便多了呢
    do
        echo  -n  "$i*$j=$(($i*$j)) "    #有一个空格
    done
    echo             #内层循环完成以后换行
done
echo


echo -e "\n"
