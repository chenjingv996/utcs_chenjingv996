#!/usr/bin/python
# -*- coding:utf-8 -*-
import telnetlib
import win32api, win32con, time
from time import sleep
import random
import logging
import os
import re
#雷达信道，部分AP调频到雷达信道时候，radio会静默1分钟
#若需要关注radio down的原因，则可以将雷达信道清空或修改为非法值，如rad_channel=["aaa"]
rad_channel=["52", "56", "60", "64"]
#空闲CPU与空闲内存的%比，脚本使用top -n top_num取top_num次空闲值，
#只有连续top_num次低于以下空闲值才会报告异常
top_num = 5
#空闲CPU与空闲内存的%比
idle_cpu = 20
free_mem = 10
#软转发上限
Sirq_use = 50
#设置每轮检查间隔时间，单位分钟
check_Interval = 3
#定义出现异常时异常日志存放路径
log_dir = 'F:/BUG_File/KJ_File/'

#开局AP IP地址列表
ap_list = [
# '18.5.0.2',
# '186.0.0.118',
'172.30.111.101',
# '172.30.111.102',  #李松定位中，没有上线
'172.30.111.205',
'172.30.111.103',
'172.30.111.104',
'172.30.111.105',
'172.30.111.106',
'172.30.111.111',
'172.30.111.206',
'172.30.111.204',
'172.30.111.202',
'172.30.111.203',
'172.30.111.101'
]

#异常时将log写入文件
def write_log(host,rs,fail_check,log_dir):
    data_time = time.strftime("%Y-%m-%d", time.localtime())
    fail_time = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
    #判断目录是否存在
    file_dir = log_dir + data_time
    #不存在则创建
    isExists=os.path.exists(file_dir)
    if not isExists:
        os.makedirs(file_dir)
    filepath=file_dir + "/"+ host + '_' +fail_time + ".txt"
    file = open(filepath,'w+')
    try:
        file.write(fail_check)
        file.write(rs)
    finally:
        file.close()
    #收集log message
    try:
        now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        print("【",now_time,"】","登录",host,"获取messages日志 ...")
        tn = telnetlib.Telnet(host)
    except:
        now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        print("【错误！】",now_time,'：',host,'网络连接失败')
        print(" ")
        return False
    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    print("【",now_time,"】登录成功，正在获取日志文件....")
    tn.write(b"cat /var/log/messages\n")
    sleep(1)
    tn.write(b"exit\n")
    log = tn.read_all().decode('ascii')    
    file = open(filepath,'a+')
    try:
        file.write(log)
    finally:
        file.close() 
    now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    print("【",now_time,"】messages日志获取完成。")


#检查AP的状态信息     
def check_wrt_ap(host, user, password):
    try:
        now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        print("【",now_time,"】连接设备：" + host + " ...")
        tn = telnetlib.Telnet(host)
    except:
        now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        print(now_time,'：',host,'网络连接失败')
        print(" ")
        return False
    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    print("【",now_time,"】登录成功，正在检查....")
    if top_num > 5:
        print("【提醒】设置的TOP检查时间为",top_num,"秒，检查时间稍长，请等待....")
    tn.write(b"get system detail\n")
    sleep(0.1)
    tn.write(b"ifconfig br-lan\n")
    sleep(0.1)
    tn.write(b"uptime\n")
    sleep(0.1)
    tn.write(b"iwconfig \n")
    sleep(0.1)
    tn.write(b"ifconfig \n")
    sleep(0.1)
    #连续两次ifconfig是为了方便后续查看接口报文情况
    tn.write(b"uptime\n")
    sleep(0.1)
    tn.write(b"ifconfig \n")
    sleep(0.1)
    tn.write(b"iwlist channel\n\n")
    sleep(1)
    tn.write(b"ls /etc/corefile\n")
    sleep(0.1)
    tn.write(b"ls /etc/crashdump\n")
    sleep(0.1)
    tn.write(b"netstat -ant | grep 57777\n")
    sleep(0.1)
    tn.write(b"ps | grep dcn\n")
    sleep(0.1)
    tn.write(b"ps |grep -v grep | grep host\n")
    sleep(0.1)
    tn.write(b"ps |grep -v grep | grep uhttpd\n")
    sleep(0.1)
    tn.write(b"ps | grep -v grep |grep lbd\n")
    sleep(0.1)
    tn.write(b"ubus call portal debug '{\"display_client\":\"\"}'\n")
    sleep(2)
    top = "top -d 1 -n  " + str(top_num)
    tn.write(top.encode('ascii')+b"\n")
    sleep(3)
    tn.write(b"free\n")
    sleep(0.1)
    tn.write(b"exit\n")
    rs = tn.read_all().decode('ascii')
    
    # 退出登录，检查各项 数据
    rs_dict = {}
    rs_dict["异常重启文件"] = rs.find("/etc/crashdump: No such file or directory")
    rs_dict["coredump文件"] = rs.find("core-")
    rs_dict["coredump文件"] = -1  if rs_dict["coredump文件"] != -1 else 1
    rs_dict["无线接口速度"] = rs.find('Rate:0 kb/s')
    if rs_dict["无线接口速度"] != -1:
        # 检查出现0 kb/s时是否为雷达静默
        for r_ch in rad_channel:
            rs_dict["无线接口速度"] = 1   if rs.find('Channel ' + r_ch) else -1
    else:
        rs_dict["无线接口速度"] = 1
    
    #获取uptime时间值，检查AP重启，检查uptime时间不小于check_Interval分钟
    rs_dict["AP运行时长"] = 1
    if rs.find("days") > 0:
        if rs.find(" min,")>0:
            uptime = re.match(r'.*\sup\s+(\d+\s+days,\s+\d+\smin),\s+lo.*',rs,re.M|re.I|re.S)
        else:
            uptime = re.match(r'.*\sup\s+(\d+\s+days,\s+\d+:\d+),\s+lo.*',rs,re.M|re.I|re.S)
    elif rs.find(" min,")>0 and rs.find("days") <0:
        uptime = re.match(r'.*\d\d\s+up\s+(\d+\s+min),.*',rs,re.M|re.I|re.S)
    else:
        uptime = re.match(r'.+up\s+(\d+:\d+),\s+.*',rs,re.M|re.I|re.S)
    if uptime:
        uptime=str(uptime.group(1))
        now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        print("【",now_time,"】设备运行时长为",uptime)
        if uptime.find("min")>0 and uptime.find("days")<0:
            min=re.match(r'.*(\d+)\s+min.*',uptime)
            if min:
                if int(min.group(1)) < check_Interval:
                    rs_dict["AP运行时长"] = -1
                    print("【",now_time,"】设备运行时长小于",check_Interval,"分钟，可能出现重启")
    else:
        print ("uptime check Failed!!")
      
    #check cpu
    Cpu_Idle = re.compile(r'(\d+)%\s+idle').findall(rs)
    if Cpu_Idle:
        rs_dict["CPU利用率"] = -1
        for cpu in Cpu_Idle:
            if int(cpu) > idle_cpu:
                rs_dict["CPU利用率"] = 1
                break
        if rs_dict["CPU利用率"] == -1:
            now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
            print("【",now_time,"】",top_num,"次CPU空闲值为",Cpu_Idle)
    else:
        print ("CPU check Failed!!")
    #check memory
    # 获取总内存大小
    all_mem = re.search( r'.buffers.*Mem:\s+(\d*)\s+', rs, re.M|re.I|re.S)
    if all_mem:
       All_mem= int(all_mem.group(1))
    #检查内存
    Mem_free = re.compile(r'(\d*)K\s+free').findall(rs)
    if Mem_free:
        rs_dict["内存利用率"] = -1
        for mem in Mem_free:
            mem_idle=int(mem)*100/All_mem
            if mem_idle > free_mem:
                rs_dict["内存利用率"] = 1
                break
        if  rs_dict["内存利用率"] == -1:
            now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
            print("【",now_time,"】内存总计",All_mem,"，",top_num,"次空闲内存为",  Mem_free) 
    else:
        now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
        print("【",now_time,"】内存 check Failed!!")
    
    #check  Sirq
    Sirq = re.compile(r'(\d+)%\s+sirq').findall(rs)
    if Sirq:
        rs_dict["Sirq利用率"] = -1
        for sirq in Sirq:
            if int(sirq) < Sirq_use:
                rs_dict["Sirq利用率"] = 1
                break
        if rs_dict["Sirq利用率"] == -1:
            now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
            print("【",now_time,"】",top_num,"次Sirq空闲值为",Sirq)
    else:
        print ("Sirq check Failed!!")
    
    #检查主要进程
    rs_dict["DCN-mapd进程"] = rs.find('/usr/sbin/dcn-mapd')
    rs_dict["Portal  进程"] = rs.find('/usr/sbin/dcn-portal')
    rs_dict["TCP管理连接"] = 1 if tcp_man    else -1
    rs_dict["DCN-wifi进程"] = rs.find('/usr/sbin/dcn-wifi')
    rs_dict["Http-web进程"] = rs.find('/usr/sbin/uhttpd')
    rs_dict["DCN-Qos 进程"] = rs.find('/usr/sbin/dcn-client-qos')
    rs_dict["watchdog进程"] = rs.find('dcn-watchdog')
    rs_dict["hostapd 进程"] = rs.find('/var/run/hostapd/global')
    rs_dict["lbd     进程"] = rs.find('/usr/sbin/lbd')
    #检查AP的TCP管理连接
    tcp_man=re.match(r'.*:57777\s+ESTABLISHED.*',rs,re.M|re.I|re.S)
    #检查UBUS执行
    rs_dict["portal  配置"] = rs.find('Command failed: Not found')
    rs_dict["portal  配置"] = -1 if rs_dict["portal  配置"] != -1  else 1
    #判断各项是否异常
    for key in rs_dict:
        if rs_dict[key] < 0:
            print(" ")
            fail_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print("【",fail_time + "】" + "AP(" + ap + "):" + key + "异常")
            print(" ")
            write_log(ap,rs,fail_time + " 发现异常项: " + key,log_dir)
            win32api.MessageBox(0, fail_time + " : " + key, ap + "异常", win32con.MB_ICONWARNING)
    return True

#开始巡检
while True:
    try:
        for ap in ap_list:
            host=ap
            user = "admin"
            password = "dcn_debug"
            print(" ")
            now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
            print("------------正在检查AP: " + host + "--------------------")
            check = check_wrt_ap(host,user,password)
            if check:
                now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
                print("【",now_time,"】设备"  + host + "检查完成。")
            else:
                print(" ")
                now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
                print("【",now_time,"】设备"  + host + "检查未完成，请检查！")
                win32api.MessageBox(0, now_time + "Script Error，Please Check!", win32con.MB_ICONWARNING)
            print("------------------------------------------------------------")
            print(" ")
        #巡检间歇时间    
        for i in range(0,check_Interval-1):
            now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
            print("【",now_time,"】",str(check_Interval-i) + "分钟后继续下一轮检查")
            sleep(60)
    except:
            now_time = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
            print("【",now_time,"】巡检脚本错误")
            win32api.MessageBox(0, now_time + "：巡检出错，请检查！！！","巡检出错", win32con.MB_ICONWARNING)