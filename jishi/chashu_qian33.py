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

class ccc:
    def aaa(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []  #嵌套列表，保存最终结果
        if root is None:
            return res
        
        from collections import deque
        que = deque([root])  #队列，保存待处理的节点
        while len(que)!=0:
            lev = []  #列表，保存该层的节点的值
            thislevel = len(que)  #该层节点个数
            while thislevel!=0:
                head = que.popleft()  #弹出队首节点
                #队首节点的左右孩子入队
                if head.left is not None:
                    que.append(head.left)
                if head.right is not None:
                    que.append(head.right)
                lev.append(head.val)  #队首节点的值压入本层
                thislevel-=1
            res.append(lev)
        return res

bbb=ccc()
print(bbb.aaa([1,2,3,4,5]))

print(f'\n')
