#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 08/10/2015
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = [1]
        product = 1
        for index in range(1, len(nums)):
            product *= nums[index-1]
            output.append(product)

        product = 1
        for index in range(len(nums)-2, -1, -1):
            product *= nums[index+1]
            output[index] *= product

        return output

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4]
    print s.productExceptSelf(nums)
