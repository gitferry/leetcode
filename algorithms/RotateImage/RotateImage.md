# [Rotate Image](https://leetcode.com/problems/rotate-image/)

---

## Description

---

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?

---

题目有点脑筋急转弯的意思，不过用python还是很容易解决。[这里](https://leetcode.com/discuss/38426/seven-short-solutions-1-to-7-lines)有人写出了7种不同的方案，不过大体思路都是首先将矩阵反转，反转之后的矩阵想要达到最终的结果是沿对角线对称的，只需要A[i][j]=A[j][i]即可。

代码实现：[Rotate Image](./RotateImage.py)

