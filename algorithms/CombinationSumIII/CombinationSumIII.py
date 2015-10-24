#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 20/10/2015
'''

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.collection = []
        self.dfs(k, [], 0, n)
        return self.collection

    def dfs(self, level, current_list, last_num, n):
        if level == len(current_list) + 1:
            if n < 1 or n > 9 or n <= last_num:
                return
            else:
                self.collection.append(current_list[:]+[n])
                return

        while last_num < 9:
            last_num += 1
            if len(current_list) < level - 1:
                current_list.append(last_num)
            self.dfs(level, current_list, last_num, n - last_num)
            current_list.pop(-1)
            if n - last_num <= last_num:
                break

if __name__ == '__main__':
    s = Solution()
    k = 3
    n = 9
    print s.combinationSum3(k, n)
