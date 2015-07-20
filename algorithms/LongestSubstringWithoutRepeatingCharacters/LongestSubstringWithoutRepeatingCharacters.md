# [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## Description

---

Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

---

刚开始还以为是动态规划的题目，后来仔细审题才发现只需要遍历字符串，创建hash表就可以解决。
j
为字符串建立hash表，键为字符，值为下标。当重复字符出现的时候，计算与上次出现重复字符的开始下标的距离，并更新该字符的下标。

代码实现：[LongestSubstringWithoutRepeatingCharacters.py](./LongestSubstringWithoutRepeatingCharacters.py)