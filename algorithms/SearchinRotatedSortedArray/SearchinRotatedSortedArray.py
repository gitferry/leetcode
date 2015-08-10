#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 10/08/2015
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
	def search(self, nums, target):
		if target not in nums: return -1

		length = len(nums)
		index_map = dict(zip(nums, range(length)))

		return index_map[target]
