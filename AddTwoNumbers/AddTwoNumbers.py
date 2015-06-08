#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 08/06/2015
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
    	carry = 0
    	head = temp = ListNode(0)

    	while l1 or l2 or carry:
    		l1_val = l1.val if l1 else 0
    		if l1:
    			l1 = l1.next

    		l2_val = l2.val if l2 else 0
    		if l2:
    			l2 = l2.next

    		carry, sum_result = divmod((l1_val + l2_val + carry), 10)
    		new_node = ListNode(sum_result)
    		temp.next = new_node
    		temp = temp.next

    	return head.next