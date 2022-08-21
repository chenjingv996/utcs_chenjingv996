#! /bin/bash
path1=/home/uos



for (( a=1;a<=3;a++ ))
do  
    echo -e "第${a}次测试"
    echo -e "第${a}次测试" >> $path1/netperfH.log
    sleep 1
    netperf -H $1 -l 120 -t TCP_STREAM >> $path1/netperfH.log
    sleep 5
    netperf -H $1 -l 120 -t TCP_RR >> $path1/netperfH.log
    sleep 5
    netperf -H $1 -l 120 -t TCP_CRR >> $path1/netperfH.log
    sleep 5
    netperf -H $1 -l 120 -t UDP_STREAM >> $path1/netperfH.log
    sleep 5
    netperf -H $1 -l 120 -t UDP_RR >> $path1/netperfH.log
 
    echo -e "\n\n\n\n" >> $path1/netperfH.log
    sleep 3
done

echo ------------------------case finish !!-----------------------------------------

count=$(cat /home/uos/netperfH.log |grep   "TCP STREAM" |wc -l)

if [ $count == "3" ];then
    tcp_stream=$(cat $path1/netperfH.log |grep -A 7  "TCP STREAM" |awk '/^[0-9]/{print $NF}')
    tcp_stream1=$(echo $tcp_stream |awk '{for(i = 1; i <= NF; i++) sum += $i; print sum/NF}')
    echo -e 'tcp_stream:\t\t'$tcp_stream1 >> $path1/netperfH.log



    tcp_rr=$(cat $path1/netperfH.log |grep -A 7  "TCP REQUEST" |awk '/^[0-9]/{print $0}'|awk 'NF>2{print $NF}')
    tcp_rr1=$(echo $tcp_rr |awk '{for(i = 1; i <= NF; i++) sum += $i; print sum/NF}')
    echo -e 'tcp_rr:\t\t'$tcp_rr1 >> $path1/netperfH.log



    tcp_crr=$(cat $path1/netperfH.log |grep -A 6  "TCP Connect" |awk '/^[0-9]/{print $NF}')
    tcp_crr1=$(echo $tcp_crr |awk '{for(i = 1; i <= NF; i++) sum += $i; print sum/NF}')
    echo -e 'tcp_crr:\t\t'$tcp_crr1 >> $path1/netperfH.log



    udp_stream1=$(cat $path1/netperfH.log |grep -A 6  "UDP STREAM" |awk '/^[0-9]/{print $NF}')
    udp_stream2=$(echo ${udp_stream1} |awk '{print $1,$3,$5}'| awk '{for(i = 1; i <= NF; i++) sum += $i; print sum/NF}')
    echo -e 'udp_stream upload:\t'$udp_stream2 >> $path1/netperfH.log



    udp_stream3=$(cat $path1/netperfH.log |grep -A 6  "UDP STREAM" |awk '/^[0-9]/{print $NF}')
    udp_stream4=$(echo ${udp_stream3} |awk '{print $2,$4,$6}' |awk '{for(i = 1; i <= NF; i++) sum += $i; print sum/NF}' )
    echo -e 'udp_stream download:'$udp_stream4 >> $path1/netperfH.log



    udp_crr=$(cat $path1/netperfH.log | grep -A 7  "UDP REQUEST" |awk '/^[0-9]/{print $0}'|awk 'NF>2{print $NF}')
    udp_crr1=$(echo $udp_crr | awk '{for(i = 1; i <= NF; i++) sum += $i; print sum/NF}')
    echo -e 'udp_crr:\t\t'$udp_crr1 >> $path1/netperfH.log


    count_1=$(echo $tcp_stream | awk '{print NF}')
    count_2=$(echo $tcp_rr | awk '{print NF}')
    count_3=$(echo $tcp_crr | awk '{print NF}')
    count_4=$(echo $udp_stream1 | awk '{print NF}')
    count_5=$(echo $udp_crr | awk '{print NF}')

    if [ $count_1 == "3" ] && [ $count_2 == "3" ] && [ $count_3 == "3" ] && [ $count_4 == "6" ] && [ $count_5 == "3" ] ;then
        echo "数据检查正常"
        echo "数据检查正常" >> $path1/netperfH.log
    else
        echo "数据检查异常,测试过程数据存在缺失,可能某次测试失败"
        echo "数据检查异常,测试过程数据存在缺失,可能某次测试失败" >> $path1/netperfH.log
    fi

fi