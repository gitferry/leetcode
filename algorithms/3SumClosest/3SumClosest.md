# [3Sum Closest](https://leetcode.com/problems/3sum-closest/)


---

## Description

---

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

---

题目意思很好理解，如果直接暴力枚举的话时间复杂度是O(n3)，显然会超时，在网上看了讨论后发现一种O(n2)的方法。

首先将数组排序，枚举第一个数，另外两个数则可以从数组的两端枚举，从两端“夹逼”，直到两数相遇。

代码实现：[3Sum Closest](./3SumClosest.py)