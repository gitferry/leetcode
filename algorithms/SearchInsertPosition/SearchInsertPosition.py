#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 07/08/2015
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
	def searchInsert(self, nums, target):
		left = 0
		right = len(nums)

		while left < right:
			mid = (left + right) / 2
			if nums[mid] == target:
				return mid
			if nums[mid] < target:
				left = mid + 1
			else:
				right = mid

		return right

