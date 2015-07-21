# [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

---

## Description

---

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.

---

基础的数据结构题，由于链表是单项链表，只能从头结点开始遍历，所以需要先遍历整个链表得到节点数。知道了整个链表的节点数就可以算出从头结点开始遍历需要删除的是哪个节点。

需要注意的两种特殊情况：

* 当整个链表只有一个节点时，直接返回空
* 当需要删除的是第一个节点时，直接返回头节点的next

代码实现：[Remove Nth Node From End of List](./RemoveNthNodeFromEndofList.py)
	