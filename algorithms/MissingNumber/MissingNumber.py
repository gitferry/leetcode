#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 27/08/2015
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        first = nums[0]

        for index, num in enumerate(nums):
            if not first + index == num:
                return num-1

        if 0 not in nums:
            return 0
        else:
            return nums[-1] + 1

if __name__ == '__main__':
    s = Solution()
    nums = [0]
    print s.missingNumber(nums)
