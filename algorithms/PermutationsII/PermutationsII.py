#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 25/10/2015
'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        self.collection = []
        vis = [0] * len(nums)
        self.dfs([], 0, nums, vis)

        return self.collection

    def dfs(self, current, index, nums, vis):
        if len(current) == len(nums):
            if current not in self.collection:
                self.collection.append(current[:])
                return
            else:
                return

        index = 0
        while index < len(nums):
            if vis[index] == 0:
                current.append(nums[index])
                vis[index] = 1
                self.dfs(current, index, nums, vis)
                vis[index] = 0
                current.pop(-1)
                while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                    index += 1

            index += 1

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,2]
    print s.permuteUnique(nums)
