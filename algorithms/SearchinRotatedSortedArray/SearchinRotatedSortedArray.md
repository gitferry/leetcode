# [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

---

## Description

---

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

---

第一次做Hard难度的题，但实际难度只有Easy，用python只用两三行代码就可以解决。

题目的标签写的是binary search，也许本意是想让解题者先将数组还原，之后用binary search解决。但这样做还要考虑到恢复前后下标的关系，最后做一个转换。

于是这时python强大的映射类型（字典）就排上用场了，只需要将原数组的元素作为键，下标作为值，构造字典，用target索引就可以直接得到结果，不存在target的键就直接return -1。

代码实现：[Search in Rotated Sorted Array](./SearchinRotatedSortedArray.py)
	