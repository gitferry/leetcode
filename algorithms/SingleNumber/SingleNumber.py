#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 06/10/2015
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        single_number = nums[0]

        for each_num in nums[1:]:
            single_number ^= each_num

        return single_number

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 2, 3]
    print s.singleNumber(nums)
