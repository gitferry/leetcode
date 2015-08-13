#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 18/07/2015
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        length = len(nums)
        min_result = nums[0] + nums[1] + nums[2]

        for i in range(length - 2):
            j, k = i+1, length-1
            while j < k:
                sum_result = nums[i] + nums[j] + nums[k]

                if sum_result == target:
                    return target

                if abs(sum_result - target) < abs(min_result - target):
                    min_result = sum_result

                if sum_result > target:
                    k -= 1
                else:
                    j += 1

        return min_result

if __name__ == '__main__':
    s = Solution()
    nums = [-1, 2, 1, -4]
    target = 1
    print s.threeSumClosest(nums, target)

