#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 10/10/2015
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        for index, node in enumerate(self.sortedTree(root)):
            if index + 1 == k:
                return node.val

    def sortedTree(self, current_node):
        """
        :type current_node: TreeNode
        :type current_k: int
        :rtype: int
        """

        if current_node.left:
            for i_node in self.sortedTree(current_node.left):
                yield i_node

        yield current_node

        if current_node.right:
            for i_node in self.sortedTree(current_node.right):
                yield i_node
