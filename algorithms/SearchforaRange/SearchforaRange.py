#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 08/08/2015
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
	def searchRange(self, nums, target):
		left, right = 0, len(nums)
		target_left = target_right = -1

		while left < right:
			mid = (left + right) / 2

			if nums[mid] == target:
				target_left = target_right = mid

				# search left border
				while target_left - 1 >= 0:
					if nums[target_left - 1] == target:
						target_left -= 1
					else:
						break

				# search right border
				while target_right + 1 < len(nums):
					if nums[target_right + 1] == target:
						target_right += 1
					else:
						break
				break

			elif nums[mid] < target:
				left = mid + 1
			else:
				right = mid

		return [target_left, target_right]

