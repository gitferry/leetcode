# [Remove Element](https://leetcode.com/problems/remove-element/)

---

## Description

---

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

---

从数组中删除目标元素，跟[26题](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)类似，但更简单。首先将数组排序，之后从第一个与目标相等的元素开始删，直到不相等。

代码实现：[Remove Element](./RemoveElement.py)
	