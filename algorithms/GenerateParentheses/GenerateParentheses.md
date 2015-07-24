# [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

---

## Description

---

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

---

解决这道题的方法有很多，我这里是用DFS解决的。

左括号与右括号都应该是n个，用这个作为搜索结束的条件。首先尝试添加左括号，当左括号多余右括号时尝试添加右括号。

代码实现：[Generate Parentheses](./GenerateParentheses.py)
	