# [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

---

## Description

Reverse a singly linked list.

---

题目可以分别用迭代和递归两种方法解决。

>   1. **递归法** 递归法也很好理解，将当前节点以后的节点看做一个整体，当只有一个节点时返回。

>   2. **迭代法** 只需要不断做交换即可。下一个与前一个节点交换，前一个和当前节点交换，当前与下一个节点交换。使用python只需要一行代码。

---

代码实现：

[Reverse Linked List with recursive method](./ReverseLinkedList1.py)
[Reverse Linked List with iterative approach](./ReverseLinkedList2.py)
