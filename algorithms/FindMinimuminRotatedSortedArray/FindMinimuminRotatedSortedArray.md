# [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

---

## Description

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

---

虽然用python的sorted()函数可以一行代码解决问题，但还是不要那么偷懒。比较容易想到的方法应该就是二分查找了，实际上就是找到数组中的“断层”。

---

代码实现：[Find Minimum in Rotated Sorted Array](./FindMinimuminRotatedSortedArray.py)

