# [Peeking Iterator](https://leetcode.com/problems/peeking-iterator/)

---

## Description

Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

---

这道题目就是在原有Iterator类的基础上进行封装，实现一个peek()函数。当执行peek()的时候返回值与next()函数相同，但并没有真正移向下一项。实现方法就是将iterator拷贝副本，返回副本的next()。

---

代码实现：[Peeking Iterator](./PeekingIterator.py)

