#/usr/bin/bash

echo -e "\n*x7_sing*.log\n"
cat -n *x7_sing*.log | egrep 'time is|elapsed|\++' && cat -n *x7_sing*.log | grep ++ | wc -l

echo -e "\n*x7_mult*.log\n"
cat -n *x7_mult*.log | egrep 'time is|elapsed|\++' && cat -n *x7_mult*.log | grep ++ | wc -l

