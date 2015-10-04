# [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

---

## Description

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

---

非常经典的题目，有很多种方法可以解决，时间复杂度也不一样。枚举的方法就不说了，这里主要介绍一下分治法和动态规划法。

> 1.    *分治法。*在这道题目中可以将整个数列划分成三个部分，分别是左半部分，右半部分，及横跨左半部分和右半部分的部分。取这三部分的最大值即可。通过递归，将问题由繁化简，最终求出整个数列的最大子序列和。时间复杂度为N(nlogn)
> 2.    *动态规划法。* 动态规划法可以将问题在线性时间内求解，代码也比较简单，但相对难理解。关键的地方就在于，当之前序列和小于0时就对之后的序列没有贡献，这时就可以抛弃之前所累加的序列和。

---

代码实现：

[Maximum Subarray(divide-and-conque)](./MaximumSubarray1.py)
[Maximum Subarray(dynamic)](./MaximumSubarray2.py)

