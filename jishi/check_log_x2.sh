#/usr/bin/bash

echo -e "\n*x2_sing*.log\n"
cat -n *x2_sing*.log | egrep 'time is|elapsed|\++' && cat -n *x2_sing*.log | grep ++ | wc -l

echo -e "\n*x2_mult*.log\n"
cat -n *x2_mult*.log | egrep 'time is|elapsed|\++' && cat -n *x2_mult*.log | grep ++ | wc -l

