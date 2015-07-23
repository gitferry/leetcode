#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 23/07/2015
'''


class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def removeDuplicates(self, nums):
		hash_table = {}
		length = len(nums)

		if length <= 1: return length

		for index in range(length):
			while index < length-1 and nums[index] == nums[index+1]:
				nums.pop(index)
				length -= 1

		return len(nums)


if __name__ == '__main__':
	s = Solution()
	nums = [1, 1, 1]
	print s.removeDuplicates(nums)