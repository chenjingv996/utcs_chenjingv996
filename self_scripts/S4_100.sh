#！/bin/bash
read -p "请输出休眠次数:" number
echo "3秒后开始休眠活动"
sleep 3
num=1
while true
do 
sudo rtcwake -l -m disk -s 60; dmesg | egrep "error|failed|warning" >> ./S4.log 
echo 第 "$num"次测试。。。 >> ./S4.log
sleep 5 ; 
echo 第 "$num"次测试。。。
num=`expr $num + 1 `
if [ $num -gt $number ];then
times=`expr $num - 1 `
echo 完成休眠测试，总共$times次。
break
fi 
done
