#!/usr/bin/env python
#coding:utf-8

class Solution:
    def addTwoNumbers(self, l1: [list], l2: [list]) -> [list]:
        head_node = list(0)
        node = head_node
        carry = 0
        while l1 !=None or l2 != None:
            l1_num = l1.val if l1 != None else 0
            l2_num = l2.val if l2 != None else 0
            num = (l1_num + l2_num + carry)%10
            carry = 1 if l1_num + l2_num + carry>= 10 else 0
            node.next = list(num)
            node = node.next
            l1 = l1.next if l1 !=None else None
            l2 = l2.next if l2 !=None else None
        if carry == 1:
            node.next = list(1)
        head_node = head_node.next
        return head_node


print(Solution().addTwoNumbers([1,3,5,7],[11,22,33,44]))
