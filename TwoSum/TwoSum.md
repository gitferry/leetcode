# [Two Sum](https://leetcode.com/problems/two-sum/)

---

## Description
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

---

这道题我能想到的共用三种方法解决，首先最容易想到的是两层循环遍历数组，O(n2)的时间复杂度，O(1)的空间复杂度，然而这种方法当数据量很大的时候会超时。

接下来稍好一点的方法是两端夹逼法，即先对数组进行排序，之后分别从两端遍历数组，当比结果大的时候，高位降低，当比结果小的时候，低位增加。然而这个方法需要主要的一点是最后返回的结果应该是排序之前的下标。排序的时间复杂度是O(logn)，查找的时间复杂度是O(n)，最终的时间复杂度是O(nlogn)


代码实现：[TwoSum.py](./TwoSum/TwoSum.py)

更好一点的方法是哈希表的方法，即对数组创建hash表，每个数作为键，下标作为值，复杂度是O(n)。需要注意的是，样例中可能出现多个相同的数，我的处理方法是，每个键对应值是一个数组，当出现相同的数的时候，存多个下标。


代码实现：[TwoSumHash.py](./TwoSum/TwoSumHash.py)

在网上的讨论中看到一个处理出现相同的数的讨巧的方法，将target-num[i]作为键，i作为值存入，这样当处理到下一个num[i]的时候，i就是第二个数的下标。


代码实现：[TwoSumHashII.py](./TwoSum/TwoSumHashII.py)

