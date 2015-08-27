# [Ugly Number](https://leetcode.com/problems/ugly-number/)

---

## Description

---

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

---

首先计算出num的素因子列表，之后遍历该列表是否存在[2, 3, 5]之外的数即可。需要注意的是1是ugly number，而非正数都不是ugly number。

代码实现：[Ugly Number](./UglyNumber.py)

