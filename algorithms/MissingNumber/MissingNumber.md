# [Missing Number](https://leetcode.com/problems/missing-number/)

---

## Description

---

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

---

首先将数组排序，选取第一个数作为基准，遍历数组，当基准加上当前的index与当前的数不相等时说明找到了缺失的数。需要注意的是，数组中必定会有0，否则缺失的就是0。

代码实现：[Missing Number](./MissingNumber.py)

