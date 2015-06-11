#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 11/06/2015
'''

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
    	minus = 0
    	x_string_reversed = str(x)[::-1]
    	if '-' in x_string_reversed:
    		x_string_reversed = x_string_reversed[:-1]
    		minus = 1
    	x_int_reversed = int(x_string_reversed)
    	if minus:
    		x_int_reversed = - x_int_reversed
    	return 0 if x_int_reversed > 2**31 or x_int_reversed < -2**31 else x_int_reversed

if __name__ == '__main__':
	solution = Solution()
	print solution.reverse(-1000000003)
