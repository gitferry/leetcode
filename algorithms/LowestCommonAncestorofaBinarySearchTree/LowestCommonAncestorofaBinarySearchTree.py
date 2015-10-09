#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 09/10/2015
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if p.val > q.val:
            tmp_node = p
            p = q
            q = tmp_node

        if root.val == q.val or root.val == p.val:
            return root
        if root.val < q.val and root.val > p.val:
            return root
        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

