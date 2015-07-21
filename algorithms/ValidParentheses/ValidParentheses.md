# [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

---

## Description

---

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

---

基础的数据结构题，训练栈的应用。

遍历字符串中每一个字符，如果当前字符在栈内有匹配的括号，则将栈推出一个元素，否则将该字符推入栈内。遍历结束后如果栈为空则说明完全匹配，否则有错。

代码实现：[Valid Parentheses](./ValidParentheses.py)
	