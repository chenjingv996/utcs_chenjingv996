#!/bin/bash

curr_time=`date +%F\ %T`

commit_git(){
    echo -e "\n当前时间为:${curr_time}\n"
    echo -e "$(date +%F\ %T)\n"
    
    git status
    echo -e "\n"
    
    cat ~/.gitconfig
    echo -e "\n"
    
    git add . && git commit -m "update_0820" && git push
    echo -e "\n\ngit提交后状态为:\n"
    
    git status
}


commit_git
