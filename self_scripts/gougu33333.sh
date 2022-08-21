#!/bin/bash


for i in `seq 50`
do	
    for j in `seq $i 50`
    do	    
	for k in `seq $j 50`
        do
            a=$((i*i))
	    b=$((j*j))
	    c=$((k*k))
	    d=$(($a+$b))
	    if [[ $c = $d ]] && [[ $c % $b = 1 ]] && [[ $c % $a = 1 ]]
        then
            echo -e "($i $j $k)"
	fi
        done
    done
done



