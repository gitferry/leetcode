# [Container With Most Water](https://leetcode.com/problems/Container-With-Most-Water/)

---

## Description

---

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

---

如果采用暴力的方法枚举的话，时间复杂度是O(n2)，可能会超时。

水的容量取决于两个条件，一个是宽度，另一个是高度，高度我们一开始无法找到最优，但宽度可以。于是我们可以首先从两端取点，当点在两端时，宽度最长。之后比较两点的高度，选取高的一边，往中间收缩，直到两边重合。

代码实现：[Container With Most Water](./ContainerWithMostWater.py)
