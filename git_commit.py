#!/usr/bin/env python
#coding:utf-8


from datetime import datetime
from time import sleep
import os
import subprocess

def git_commit():
    print("#"*50)
    print(os.system("git status"))
    print()
    print(os.system("cat ~/.gitconfig"))
    print()
    print(os.system("git add . && git commit -m \"update_0820\" && git push"))
    print()
    print("提交后的状态为:")
    print()
    print(os.system("git status"))
    print()

def git_push():
    print("#"*50)
    print(subprocess.call("./commit_git.sh"))
    print()


if __name__=="__main__":
    #git_commit()
    git_push()
