# [Reverse Integer](https://leetcode.com/problems/reverse-integer/)

---

## Description

---

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Update (2014-11-10):
Test cases had been added to test the overflow behavior.

---

python在处理大数时几乎不需要考虑overflow的问题，但这道题当处理大于32位的数时要返回零。

这道题没有什么难度，python在类型转换方面都有现成的库，只需要注意当数是负数的情况。

我的实现感觉稍微有点麻烦，看了discuss发现有1行就可以解决的代码，但其实思路都一样。

最近机缘巧合得到了一个可以免试参与三星暑期实习的机会，希望在实习之前能在算法上有所提高。

代码实现：[ReverseInteger.py](./ReverseInteger.py)