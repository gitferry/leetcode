#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 16/10/2015
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, mid, right = 0, 0, len(nums) - 1
        while left < right:
            mid = (left + right) / 2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid

        return nums[left]
