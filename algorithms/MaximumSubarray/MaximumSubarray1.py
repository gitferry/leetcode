#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 01/10/2015
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        temp_sum = max_sum = 0
        for num in nums:
            temp_sum += num
            if temp_sum > max_sum:
                max_sum = temp_sum
            elif temp_sum < 0:
                temp_sum = 0

        if max_sum == 0:
            max_sum = max(nums)

        return max_sum

if __name__ == '__main__':
    s = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    print s.maxSubArray(nums)
