# [Permutations](https://leetcode.com/problems/permutations/)

---

## Description

---

Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

---

最基础的搜索题，我采用dfs做的。

首先设置一个visit字典，键是数组中的每个数，值为1或0分别表示该数有或没有被选取过。每次搜索将一个数入栈，并把对应的visit键值设为1，搜索结束将该数推出栈，并还原visit键值。

代码实现：[Permutations](./Permutations.py)

