#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 04/10/2015
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length = len(nums)
        if length == 1: return nums[0]

        mid_pos = length / 2

        max_sum_left = self.maxSubArray(nums[0:mid_pos])
        max_sum_right = self.maxSubArray(nums[mid_pos:length])

        # left max sum with border
        border_left_max_sum = nums[mid_pos-1]
        border_left_sum = 0
        for each_num in nums[:mid_pos][::-1]:
            border_left_sum += each_num
            border_left_max_sum = max(border_left_sum, border_left_max_sum)

        # right max sum with border
        border_right_max_sum = nums[mid_pos]
        border_right_sum = 0
        for each_num in nums[mid_pos:]:
            border_right_sum += each_num
            border_right_max_sum = max(border_right_sum, border_right_max_sum)

        print border_left_max_sum, border_right_max_sum
        return max(max_sum_left, max_sum_right, border_left_max_sum+border_right_max_sum)


if __name__ == '__main__':
    s = Solution()
    nums = [8,-19,5,-4,20]

    print s.maxSubArray(nums)
