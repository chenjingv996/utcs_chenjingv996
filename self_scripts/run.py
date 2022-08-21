#!/usr/bin python3
#*-*coding:utf-8
import time
import os

print(
    """
    #readme
    #1 操作系统安装用户名为uos，密码1
    #2 将脚本放在/home/uos/下
    #3 设置帐号自动登录，无密码登录(脚本已实现)
    #4 设置电源管理设置关闭显示器、进入待机时间、自动锁屏时间设置成从不，保证显示屏常亮
    #5 关闭窗口特效
    #6 切换为root账号，执行：python3 run.py
    #7 执行过程中不做任何其他操作...
    """
    )

time.sleep(60)

os.environ['DISPLAY'] = ':0'
os.system("apt update")
os.system("apt install python3-pip libjpeg-dev zlib1g-dev -y")
all = os.popen("pip3 list").read()
if "PyAutoGUI" in all:
    print("存在 PyAutoGUI 库")
else:
    print("不存在 PyAutoGUI 库")
    os.system("pip3 install pyautogui xlrd xlwt -i https://pypi.douban.com/simple/")

# 安装必要库
os.system("apt-get install python3-tk -y")
listdir=os.listdir("/home/uos/")
if "PerformanceTest_reboot.sh" in listdir:
    print("存在 PerformanceTest_reboot.sh 脚本")
else:
    print("不存在 PerformanceTest_reboot.sh 脚本")
    os.system("wget -O /home/uos/PerformanceTest_reboot.sh http://10.20.49.246:8888/test/Perf/PerformanceTest_reboot.sh")
    os.system("wget -O /home/uos/PerformDataDeal.py http://10.20.49.246:8888/test/Perf/PerformDataDeal.py")
time.sleep(5)
os.system("chmod 777 /home/uos/PerformanceTest_reboot.sh")
os.system("chmod 777 /home/uos/run.py")

#不能将这个import移动到文件开头！！！
import pyautogui
pyautogui.FAILSAFE = False
# 打开终端
pyautogui.hotkey("ctrl", "alt","t")
time.sleep(10)
if "set.conf" not in listdir:
    # 关闭窗口特效
    pyautogui.typewrite(message="dbus-send --session --dest=com.deepin.wm --print-reply /com/deepin/wm org.freedesktop.DBus.Properties.Set string:com.deepin.wm string:compositingEnabled variant:boolean:false", interval="0.05")
    time.sleep(2)
    pyautogui.press("enter", interval=0.25)
    time.sleep(2)
    pyautogui.press("esc", interval=0.25)
    pyautogui.press("enter", interval=0.25)
    time.sleep(2)

    # 设置待机时间为从不
    pyautogui.typewrite(message="dbus-send --session --dest=com.deepin.daemon.Power --print-reply /com/deepin/daemon/Power org.freedesktop.DBus.Properties.Set string:com.deepin.daemon.Power string:LinePowerSleepDelay variant:int32:0", interval="0.05")
    time.sleep(2)
    pyautogui.press("enter", interval=0.25)
    time.sleep(2)

    # 设置锁定时间为从不
    pyautogui.typewrite(message="dbus-send --session --dest=com.deepin.daemon.Power --print-reply /com/deepin/daemon/Power org.freedesktop.DBus.Properties.Set string:com.deepin.daemon.Power string:LinePowerLockDelay variant:int32:0", interval="0.05")
    time.sleep(2)
    pyautogui.press("enter", interval=0.25)
    time.sleep(2)

    # 设置锁定时间为从不
    pyautogui.typewrite(message="dbus-send --session --dest=com.deepin.daemon.Power --print-reply /com/deepin/daemon/Power org.freedesktop.DBus.Properties.Set string:com.deepin.daemon.Power string:LinePowerScreenBlackDelay variant:int32:0", interval="0.05")
    time.sleep(2)
    pyautogui.press("enter", interval=0.25)
    time.sleep(2)

    os.system("echo 1 > /home/uos/set.conf")

# 切换到root用户
pyautogui.typewrite(message="sudo su", interval="0.25")
time.sleep(2)
pyautogui.press("enter", interval=0.25)
time.sleep(2)
pyautogui.typewrite(message="1", interval="0.25")
time.sleep(2)
pyautogui.press("enter", interval=0.25)
time.sleep(2)
pyautogui.typewrite(message="bash /home/uos/PerformanceTest_reboot.sh 2>&1 |tee -a run.log", interval="0.25")
time.sleep(2)
# 回车运行
pyautogui.press("enter", interval=0.25)
