# [Unique Paths](https://leetcode.com/problems/unique-paths/)

---

## Description

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

![](http://articles.leetcode.com/wp-content/uploads/2014/12/robot_maze.png)

---

很基础的动态规划题，递推公式为dp[i][j] = dp[i-1][j]+dp[i][j-1]，这是因为每个终点的路径数都是由左边和上边的终点的路径数只和得到的。

当终点落在上边和左边上时，路径数为1。

另外有一种O(1)的方法就是中学时学的排列组合法，由于只能向右和向下，于是总共有(m+n-2)种可能，其中选(m-1)种向下，(n-1)种向右，利用排列组合公式即可解决。

---

代码实现：

[Unique Paths With Permutations](./UniquePaths1.py)
[Unique Paths With Dynamic Program](./UniquePaths2.py)

