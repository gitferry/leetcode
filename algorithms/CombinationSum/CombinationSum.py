#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 13/08/2015
'''

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        com_list = []
        candidates.sort()
        self.dfs(candidates, target, [], 0, com_list)
        return com_list

    def dfs(self, candidates, remain, current, index, com_list):
        if remain == 0:
            if current not in com_list:
                com_list.append(current[:])
        if remain < 0 or candidates[index] > remain:
            return
        while index < len(candidates):
            current.append(candidates[index])
            self.dfs(candidates, remain - candidates[index], current, index, com_list)
            current.pop()
            if candidates[index] > remain:
                break
            index += 1


if __name__ == '__main__':
    s = Solution()
    candidates = [2, 2, 3, 7]
    target = 7
    print s.combinationSum(candidates, target)
