# [Single Number](https://leetcode.com/problems/single-number/)

---

## Description

Given an array of integers, every element appears twice except for one. Find that single one.

---

用普通的方法可能会超时，这里可以根据这道题利用异或的特性，在线性时间内解决。

这里用到的异或的特性有两点：

>   1.和自身异或运算得0
>   2.和0异或运算得自身

这道题目的特点是只有一个数出现一次，且其它所有数都出现两次。这样就可以用到异或运算的特性，将所有数一起异或，得到的最后结果就是只出现一次的那个数。

---

代码实现：[Single Number](./SingleNumber.py)

