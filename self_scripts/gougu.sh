#!/bin/bash

fun_timer()
{
    echo -e "\n"
    echo -e "当前时间为:"$(date "+%Y-%m-%d %H:%M:%S")
}

fun_start()
{
    echo -e "\n"
    echo -e "################################################"
}

fun_end()
{
    echo -e "\n"
    echo -e "################################################"
}

fun_gougu()
{
    fun_start
    printf "my name is chenjingv!\n"
    for i in `seq 100`
    do 
        for j in `seq $i 100`
        do 
        a=$((i*i))		
    fun_end
}

main_menu()
{    
    fun_timer 
    fun_gougu
}


main_menu



