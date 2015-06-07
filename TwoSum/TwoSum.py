#!/usr/bin/env python
# coding=utf-8

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
    	nums_dict = dict(zip(range(len(nums)), nums))
    	nums = sorted(nums_dict.items(), key=lambda nums_dict:nums_dict[1])
    	tail = len(nums) - 1
    	begin = 0
    	while begin < tail:
    		two_sum = nums[begin][1] + nums[tail][1]
    		if two_sum == target:
    			return sorted([nums[begin][0] + 1, nums[tail][0] + 1])
    		elif two_sum > target:
    			tail -= 1
    		else:
    			begin += 1


if __name__ == '__main__':
    solution = Solution()
    nums = [-1,-2,-3,-4,-5]
    target = -8
    twoNum = solution.twoSum(nums, target)

    print twoNum
