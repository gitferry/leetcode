#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 17/10/2015
'''

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        bit_map = 0
        for num in nums:
            target_bit = (bit_map >> num) & 1
            if target_bit == 0:
                bit_map |= (1 << num)
            else:
                return num


