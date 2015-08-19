# [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

---

## Description

---

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

---

双指针的题，我的方法是从左边开始，另一个指针向后搜索，如果小于当前的就假设要存水，大于当前的就把之前假设的加上，其中有几种需要注意的特殊情况。这种方法有点笨了，看讨论里大部分都是从两边开始向里收缩，代码要简单许多。

代码实现：[Trapping Rain Water](./TrappingRainWater.py)

