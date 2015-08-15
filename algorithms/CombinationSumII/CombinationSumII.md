# [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

---

## Description

---

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]

---

跟[Combination Sum](https://leetcode.com/problems/combination-sum/)不同的是挑选过的数不能重复挑选，只需要在此基础上添加一个字典vis用来记录该数是否被挑选就可以了，需要注意回溯的时候要把vis还原。

代码实现：[Combination Sum II](./CombinationSumII.py)

