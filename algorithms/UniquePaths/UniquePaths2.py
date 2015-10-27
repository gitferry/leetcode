#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 27/10/2015
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        db = [[1 for col in range(100)] for row in range(100)]

        for i in xrange(1, m):
            for j in xrange(1, n):
                db[i][j] = db[i-1][j] + db[i][j-1]

        return db[m-1][n-1]

if __name__ == '__main__':
    s = Solution()
    m = 3
    n = 3
    print s.uniquePaths(m, n)

