# [Combination Sum](https://leetcode.com/problems/combination-sum/)

---

## Description

---

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]

---

典型的回溯题，需要注意的是得到的结果中不能有重复的出现，这就要保证在搜索的时候只搜比当前数大的数。

代码实现：[Combination Sum](./CombinationSum.py)

