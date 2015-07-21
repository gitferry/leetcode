#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 21/07/2015
'''

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
	def removeNthFromEnd(self, head, n):
		node = head
		node_counts = 0
		while node != None:
			node_counts += 1
			node = node.next

		if node_counts == 1:
			return None

		if node_counts == n:
			return head.next

		index = 0
		node = ListNode(0)
		node.next = head

		while node != None:
			if index == node_counts - n:
				node.next = node.next.next
				break

			index += 1
			node = node.next

		return head

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
	nodes = [1, 2]
	head = s.createNodes(nodes)

	s.removeNthFromEnd(head, 2)
