#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
    	length = len(nums)
    	num_dict = {}

    	# create hash map
    	for index in xrange(length):
    		if num_dict.has_key(nums[index]):
    			num_dict[nums[index]].append(index)
    		else:
    			num_dict[nums[index]] = [index]

    	# find two sum
    	for index in xrange(length):
    		gap = target - nums[index]
    		if num_dict.has_key(gap):
	    		if index in num_dict[gap]:
	    			if len(num_dict[gap]) > 1:
		    			index_two = num_dict[gap][1]
		    		else:
		    			continue
	    		else :
	    			index_two = num_dict[gap][0]
	    		return [index + 1, index_two + 1]


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 4]
    target = 6
    twoNum = solution.twoSum(nums, target)

    print twoNum