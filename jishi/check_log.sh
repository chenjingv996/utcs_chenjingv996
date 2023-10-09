#/usr/bin/bash

echo -e "\n*sing*.log\n"
cat -n *sing*.log | egrep 'start|\++' && cat -n *sing*.log | grep ++ | wc -l

echo -e "\n*mult*.log\n"
cat -n *mult*.log | egrep 'start|\++' && cat -n *mult*.log | grep ++ | wc -l

