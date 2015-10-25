# [Permutations II](https://leetcode.com/problems/permutations-ii/)

---

## Description

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

---

跟前一道[Permutations](https://leetcode.com/problems/permutations/)思路基本一样，但不同的是这道题会有重复的数，但最后的组合不能有重复的，如果还按之前的方法做会超时。

这里采用的方法是，先对数组排序，这样相同的数都排在一起，回溯的时候跳过相同的数就可以了。

---

代码实现：[Permutations II](./PermutationsII.py)

