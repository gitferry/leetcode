#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 05/10/2015
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        index = 0
        while index < length:
            while index < length and nums[index] == 0:
                nums.pop(index)
                length -= 1
                nums.append(0)

            index += 1

        return nums

if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1]
    print s.moveZeroes(nums)

