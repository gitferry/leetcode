#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 13/06/2015
'''

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
    		return str(x)[::-1] == str(x)


if __name__ == '__main__':
	solution = Solution()
	print solution.isPalindrome(121)