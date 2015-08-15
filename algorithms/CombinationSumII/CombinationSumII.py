#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 15/08/2015
'''

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()
        vis = dict(zip(range(len(candidates)), [0] * len(candidates)))
        collection = []
        self.dfs(candidates, [], target, collection, vis, 0)
        return collection

    def dfs(self, candidates, current, remain, collection, vis, index):
        if remain == 0:
            if current not in collection:
                collection.append(current[:])
            return
        if remain > 0:
            while index < len(candidates):
                if not vis[index]:
                    current.append(candidates[index])
                    vis[index] = 1
                    self.dfs(candidates, current, remain - candidates[index], collection, vis, index)
                    current.pop()
                    vis[index] = 0
                    if candidates[index] > remain:
                        break
                index += 1



if __name__ == '__main__':
    s = Solution()
    candidates = [10,1,2,7,6,1,5]

    target = 8

    print s.combinationSum2(candidates, target)
