# [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

---

## Description

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:

    You must not modify the array (assume the array is read only).

    You must use only constant, O(1) extra space.

    Your runtime complexity should be less than O(n2).

    There is only one duplicate number in the array, but it could be repeated more than once.

---

题目限制比较大，无法对原数组排序，也不能创建多余的数组，因此这里采用一个比较讨巧的方法。得益于python的整型所占字节数非常大，我们可以将一个整型变量当做一个哈希表，每一位0、1表示这一位的数是否出现过。

---

代码实现：[Find the Duplicate Number](./FindtheDuplicateNumber.py)

