#!/bin/bash

git status
echo -e "\n"

cat ~/.gitconfig
echo -e "\n"

git add . && git commit -m "update_0820" && git push
echo -e "\n\ngit提交后状态为:\n"

git status
