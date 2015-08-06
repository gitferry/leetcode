#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 06/08/2015
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
	def removeElement(self, nums, val):
		nums.sort()
		length = len(nums)

		for index in range(length):
			while index < length and nums[index] == val:
				nums.pop(index)
				length -= 1

		return length
