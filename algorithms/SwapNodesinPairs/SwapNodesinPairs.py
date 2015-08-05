#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 05/08/2015
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
	def swapPairs(self, head):
		n0 = ListNode(0)
		n0.next = head

		node = n0
		while node.next != None:
			if node.next.next == None:
				break

			n1 = node.next
			n2 = n1.next

			node.next = n2
			n1.next = n2.next
			n2.next = n1

			node = node.next.next

		return n0.next

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
	nodes = [1, 2, 3, 4]
	head = s.createNodes(nodes)

	s.swapPairs(head)
