#!/usr/bin/env python
#coding:utf-8

print("#"*80+"\n")

import time
from datetime import datetime as dt
import sys
import re
import math

print(f"{time.ctime()}\n")
print(f'{dt.now().strftime("%Y-%m-%d %H:%M:%S")}\n')

class Solution:
# 前序
	def preorderTraversal(self, root: TreeNode) -> list[int]:
		result = []       # 用于存放结果
		stack = [root]    # 把root节点存入栈中
		if stack == None: # 检测结点为空的情况
			return []
		while stack:      # 当栈为空的时候，说明已经遍历完成
			node = stack.pop() # 弹出root节点
			result.append(node.val)  # 先处理中间节点
			if node.right:     # 再处理右孩子，因为右边先入栈，左边再入栈，出栈的时候才是先左再右
				stack.append(node.right)
			if node.left:      # 最后处理左节点
				stack.append(node.left)
		return result



print(f'\n')
