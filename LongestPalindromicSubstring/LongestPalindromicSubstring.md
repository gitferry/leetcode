# [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

---

## Description

---

Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

---

前段时间忙毕业设计，毕业设计忙完了又要处理离校前的各种手续，跟朝夕相处了4年的朋友、老师告别，各种聚会络绎不绝，脑袋在酒精的反复作用下一直没有很清醒过。然而，该结束的总会结束的，该坚持的还是要继续坚持。

非常经典的最长回文子串问题，最容易想到的方法是枚举所有的子串判断是否是回文字符串，之后选出最长的，复杂度为O(n2)。这种方法用python实现后会超时。

通过查看leetcode上的讨论区发现一种O(n)的算法，称作Manacher算法。算法的核心思想就是利用之前比较的结果来减少后续比较的次数，有点像动态规划。算法的具体实现原理可以参照这一篇[文章](http://www.felix021.com/blog/read.php?2040#3770)。


代码实现：[Longest Palindromic Substring](./LongestPalindromicSubstring.py)