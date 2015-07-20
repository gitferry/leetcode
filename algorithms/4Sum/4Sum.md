# [4Sum](https://leetcode.com/problems/4sum/)

---

## Description

---

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

---

按着3Sum的思路来做，只是多了一层循环，时间复杂度是O(n3)。

本以为会超时，但实际上并没有，看讨论上也没有发现更好的方法了。

代码实现：[4Sum](./4Sum.py)
	