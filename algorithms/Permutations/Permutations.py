#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 14/08/2015
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        visit = dict(zip(nums, [0]*len(nums)))
        collection = []
        self.dfs(nums, [], collection, visit)
        return collection

    def dfs(self, nums, current, collection, visit):
        if len(current) == len(nums):
            collection.append(current[:])
            return
        if len(current) < len(nums):
            for num in nums:
                if not visit[num]:
                    current.append(num)
                    visit[num] = 1
                    self.dfs(nums, current, collection, visit)
                    visit[num] = 0
                    current.pop()

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print s.permute(nums)
