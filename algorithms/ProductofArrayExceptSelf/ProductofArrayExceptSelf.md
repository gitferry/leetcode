# [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

---

## Description

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

---

题目要求不能使用除法，而且要在O(n)时间内完成。基于此我们可以正反两次遍历数组来完成，正向遍历时将当前数与之前数的乘积放入output[i]，反向遍历时将output[i]与剩余的数相乘。

---

代码实现：[Product of Array Except Self](./ProductofArrayExceptSelf.py)

