#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#ltp功能测试自动化脚本
#########################################################
# Function :LTP test                                    #
# Platform :Uniontech OS                                #
# Version  :1.0                                         #
# Date     :2021-01-25                                  #
# Author   :guobin                                      #
# Contact  :guobin@uniontech.com                        #
# Company  :UnionTech                                   #
#########################################################

import os
import sys
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def user_auth():
    if os.getuid() == 0:
        pass
    else:
        print("当前用户不是root，请以root用户执行脚本")
        sys.exit(1)


def command(cmd):
    res = os.system(cmd)
    if res != 0:
        print("%s:执行失败" % cmd)
        sys.exit(1)
    else:
        print("%s:执行成功" % cmd)
        return 0

def shellReturn(cmd):
    r = os.popen(cmd)  
    text = str(r.read())
    text = text.splitlines(True)
    txt = [x.strip() for x in text]
    return ",".join(txt)



def install_ltp(option,number):
    print("开始安装ltp测试套件")
    print("="*60)
    cmd = "apt install  -y autoconf make gcc build-essential git"
    command(cmd)
    #清理已存在的 /opt/ltp目录

    if os.path.exists("/opt/ltp"):
        command("rm -rf /opt/ltp")

    #删除已存在的ltp文件
    # if os.path.exists("ltp"):
    #     command("rm -rf ltp")

    if os.path.exists("ltp"):
        pass
    else:
        #克隆ltp工程
        x = 1
        while True:
            print("开始克隆，第%s次克隆" %x)
            abc = os.system("git clone https://github.com/linux-test-project/ltp.git")
            if abc == 0 :
                print ("克隆LTP工程成功，开始装载LTP工程")
                break
            else:
                print ("克隆LTP工程失败，自动重试")
            x += 1
            
    command(cmd)
    #切换目录,使用 os.system("目录") 不能切换目录,程序执行目录
    os.chdir("ltp")
    if option == "-f":
        name = shellReturn("lscpu |awk '/Architecture:/{print $NF}'")
        '''
        #注释 /usr/include/%s-linux-gnu/sys/ustat.h 下的   %s代表当前的cpu平台--->(arm x86 mips)
            extern int ustat (__dev_t __dev, struct ustat *__ubuf) __THROW;
        #注释 /usr/include/%s-linux-gnu/bits/ustat.h 下的
            struct ustat
                {
                    __daddr_t f_tfree;          /* Number of free blocks.  */
                    __ino_t f_tinode;           /* Number of free inodes.  */
                    char f_fname[6];
                    char f_fpack[6];
                };
        '''
        resys = "sed -i  '/^extern/ s/^\(.*\)$/\/\/\1/p' /usr/include/%s-linux-gnu/sys/ustat.h " %name
        command(resys)
        rebits = "sed -i '/^struct/,+6 s/^\(.*\)$/\/\/\1/p' /usr/include/%s-linux-gnu/bits/ustat.h" %name
        command(rebits)
    
        cmd = "make autotools"
        command(cmd)
        cmd = "./configure"
        command(cmd)
        cmd = "make all"
        command(cmd)
        cmd = "make install"
        command(cmd)
        #切换目录到/opt/ltp/testscripts/
        os.chdir("/opt/ltp/")
        #执行ltp 功能测试
        os.system("bash runltp")

    elif option == "-p":

        cmd = "git checkout 20160510"
        command(cmd)
        cmd = "make autotools"
        command(cmd)
        cmd = "./configure"
        command(cmd)
        cmd = "make all"
        command(cmd)
        cmd = "make install"
        command(cmd)
        #切换目录到/opt/ltp/testscripts/
        os.chdir("/opt/ltp/testscripts")
        #输出任务开始时间
        print (time.strftime("%Y-%m-%d %H:%M:%S"))
        #执行ltp 压力测试
        os.system("bash ltpstress.sh -p -n -t %s -l /home/uos/ltp.log" %number)

        #切换到uos主目录
        os.chdir("/home/uos/")

        #执行监控程序
        os.system("bash monitor.sh")
    else:
        #参数错误代码退出
        exit()

'''
小结
根据开发反馈用例进行覆盖执行并在使用最新12-22 最新LTP包进行功能测试覆盖
与开发沟通,目前已确认剩余 已知失败测试case5个  分别是
1 sync_file_range  : 目前系统中未实现该函数
2 sync_file_range02   :ntfs不支持该系统调用)
3 memcg_use_hierarchy   : 用例判断不正确
4 getaddrinfo_01: 系统未使用ipv6网络
5 tpci tpci 在飞腾2000桌面可以测试通过,在鲲鹏机器上ltp_tpci.ko模块需要手动强制insmod才可以进入测试，且在测试pci设备时，由于pci设备可用地址空间不同，有些设备由于地址空间用尽在ltp分配地址空间时会报错
'''

#包含英文环境运行和已知风险 case
whiteList = [
    "crypto_user02","nm01_sh","file01_sh","mkdir01_sh","tpci",
    "ar_sh","getaddrinfo_01","sysctl02_sh","memcg_use_hierarchy","du01_sh",
    "memcg_stat","sync_file_range02","select03","madvise06","sync_file_range",
    "mincore04","fanotify09","fanotify09","chdir01","capget02","ustat01",
    "add_key05","stat01","stat02","leapsec01","msgstress03",
]

#获得 /opt/ltp/results 中的文件获取文件名,获取失败项
def checkFail(path):
    filelist = os.listdir(path)
    ltpname = ""
    for a in filelist:
        if "LTP_RUN_ON" in a:
            ltpname = a
    print("遍历ltp结果目录获得 LTP 文件名 : %s" %ltpname)
    with open("%s/%s" %(path,ltpname)) as f:
        fail = [line.rstrip('\n',) for line in f]

    failList = []
    for a in fail:
        if "FAIL" in a:
            b = list(filter(None, a.split("  ")))
            failList.append(b[0])
    
    return ltpname,failList

#遍历错误项 对比已知的失败项,找出未知的失败项
def contrastFail(whiteList,failList):
    unknownList = []
    for a in failList:
        if a in whiteList:
            pass
        else:
            unknownList.append(a)
    return unknownList

#发送邮件方法,传入测试结果, 已知的case ,失败的case ,未知的case
def sed_email(path,ltpname,whiteList,failList,unknownList):
    #帐号
    sender = 'guobin@uniontech.com'
    #密码
    passwd = "notice1"

    # 收件人
    receivers = [
        "guobin@uniontech.com"
        ]

    #创建一个带附件的实例
    message = MIMEMultipart()

    #发件人
    message['From'] = ("%s") % (Header('guobin@uniontech.com','utf-8'),)
    message['To'] =  ",".join(receivers)

    #邮件标题
    subject = "ltp测试结果邮件"
    message['Subject'] = Header(subject, 'utf-8')
    
    #邮件正文内容
    message.attach(MIMEText('''
    hi all:
        \t LTP 功能测试结果推送
        \t 本次测试失败项:
        %s

        \t 筛选除去已知风险后----->未知风险项:
        %s

        \t 已知风险项(已经通过研发确认):
        %s
        
        
    ''' %(failList,unknownList,whiteList), 'plain', 'utf-8'))
    
    # 构造附件1，传送当前目录下的 Performance results.xlsx 文件
    att = MIMEText(open('%s/%s' %(path,ltpname), 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att["Content-Disposition"] = 'attachment; filename="%s" ' %ltpname
    message.attach(att)
    
    # 构造附件2，传送当前目录下的 runoob.txt 文件
    # att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
    # att2["Content-Type"] = 'application/octet-stream'
    # att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
    # message.attach(att2)
    
    try:
        smtp = smtplib.SMTP("smtp.uniontech.com", timeout=30)
        smtp.login(sender,passwd)
        smtp.sendmail(sender,message["To"].split(","), message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        option = sys.argv[1]
        try:
            number = int(sys.argv[2])
        except:
            number = 0

        if option == "-f" or option == "-p":
            path = "/opt/ltp/results"
            print("测试类型======>",option,"测试时间======>",number)
            user_auth()
            install_ltp(option,number)
            time.sleep(10)
            ltpname,failList = checkFail(path)
            unknownList = contrastFail(whiteList,failList)
            sed_email(path,ltpname,whiteList,failList,unknownList)
        else:
            print('''
usage: python3 [ltp.py] <option> <optional>
例如:
    功能测试:
    python3 ltp.py -f 
    
    压力测试:
    python3 ltp.py -p times(h)

    -f  function,功能测试

    -p  pressure,压力测试 times(单位:小时)
            ''')
    else:
        print('''
usage: python3 ltp.py <option> <optional>
例如:
    功能测试:
    python3 ltp.py -f 
    
    压力测试:
    python3 ltp.py -p times(h)

    -f  function,功能测试

    -p  pressure,压力测试 times(单位:小时)
        ''')


