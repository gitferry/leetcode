# [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

---

## Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

---

找到两个节点的公共最低父节点(LCA)。由于是二叉搜索树(BST)，每个节点的右节点的值都比该节点的值大，左边的节点的值小。利用BST的性质，当前节点的值与其中一个节点的值相等时，则该节点就是LCA，如果该节点的值在两节点的值之间，则该节点也是LCA。如果该节点比较小的节点还小，说明LCA在该节点的右侧，应该从右子树开始继续搜索。如果该节点比较大的节点还大，在从左字数开始继续搜索。

---

代码实现：[Lowest Common Ancestor of a Binary Search Tree](./LowestCommonAncestorofaBinarySearchTree.py)

