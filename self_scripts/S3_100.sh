#！/bin/bash
read -p "请输出待机次数:" number
echo "3秒后开始待机活动"
sleep 3
num=1
while true
do 
sudo rtcwake -l -m mem -s 20; dmesg | egrep "error|failed|warning" >> ./S3.log 
echo 第 "$num"次测试。。。 >> ./S3.log
sleep 5 ; 
echo 第 "$num"次测试。。。
num=`expr $num + 1 `
if [ $num -gt $number ];then
times=`expr $num - 1 `
echo 完成待机测试，总共$times次。
break
fi 
done
