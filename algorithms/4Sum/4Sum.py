#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 20/07/2015
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
	def fourSum(self, nums, target):
		nums.sort()
		quadruplets = []

		length = len(nums)
		for i in range(length-3):
			for j in range(i+1, length-2):
				k, l = j+1, length - 1
				while k < l:
					sum_result = nums[i] + nums[j] + nums[k] + nums[l]

					if sum_result == target:
						one_quadruplet = [nums[i], nums[j], nums[k], nums[l]]
						if one_quadruplet not in quadruplets:
							quadruplets.append(one_quadruplet)
						l -= 1
						k += 1
					elif sum_result > target:
						l -= 1
					else:
						k += 1

		return quadruplets



if __name__ == '__main__':
	s = Solution()
	nums = [-3,-2,-1,0,0,1,2,3]
	target = 0
	print s.fourSum(nums, target)
    				
