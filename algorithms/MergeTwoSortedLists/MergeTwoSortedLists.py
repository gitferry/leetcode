#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 23/07/2015
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
	def mergeTwoLists(self, l1, l2):
		head1 = l1
		head2 = l2

		head = node = ListNode(0)

		while head1 != None or head2 != None:
			if head1 == None:
				node.next = head2
				break
			if head2 == None:
				node.next = head1
				break
			if head1.val < head2.val:
				node.next = head1
				head1 = head1.next
			else:
				node.next = head2
				head2 = head2.next
			node = node.next

		return head.next
		self.showList(head.next)


	def showList(self, head):
		node = head
		while node != None:
			print node.val
			node = node.next



	def createNodes(self, nodes):
		n = len(nodes)
		head = ListNode(0)
		last_node = head
		for i in range(n):
			node = ListNode(nodes[i])
			last_node.next = node
			last_node = node

		# self.showList(head.next)
		return head.next

if __name__ == '__main__':
	s = Solution()
	nodes1 = [1, 3, 5, 6]
	nodes2 = [0, 4, 5, 8, 9]
	head1 = s.createNodes(nodes1)
	head2 = s.createNodes(nodes2)
	s.mergeTwoLists(head1, head2)

