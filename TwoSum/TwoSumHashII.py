#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 06/07/2015
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
    	num_map = {}
    	for j, num in enumerate(nums, 1):
    		if num_map.get(num, 0):
    			return [num_map[num], j]
    		else:
    			num_map[target - num] = j


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    twoNum = solution.twoSum(nums, target)

    print twoNum