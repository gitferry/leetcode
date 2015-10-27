# [Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)

---

## Description

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

    [[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

    [[1,2,6], [1,3,5], [2,3,4]]

---

经典的回溯算法，跟之前两道Combination Sum的区别就是多了一个变量k，指定了组合数的个数，并且每个数在0-9之间，且不能有重复，每个组合按从小到大排列。算法上没有太大区别，直接看代码就好。

---

代码实现：[Combination Sum III](./CombinationSumIII.py)
