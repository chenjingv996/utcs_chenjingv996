#!/usr/bin/env python
#coding:utf-8

from datetime import datetime
import os
import time 

def git_commit():
    print("#"*50)
    print(datetime.now())
    print(os.system("git status\n")) 
    print(time.sleep(1))
    print(os.system("cat ~/.gitconfig\n"))
    print(time.sleep(1))
    print(os.system("git add . && git commit -m \"update_0820\" && git push\n"))
    print(time.sleep(1))
    print("提交状态为:\n")
    print(os.system("git push\n"))
    return git_commit
if __name__=="__main__":
    git_commit()
    
    
