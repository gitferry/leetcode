#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 16/10/2015
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        result = 0
        for i in xrange(length):
            result += (ord(s[-i-1]) - ord('A') + 1) * 26 ** i

        return result
