#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 03/07/2015
'''

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        length = len(s)
        result_string = ""

        if length == 1 or length <= numRows or numRows == 1:
        	return s

        for i in range(numRows):
        	result_string += s[i]

        	column_index = i + 2 * numRows - 2

        	while column_index - 2 * i < length:
        		if i != 0 and i != numRows - 1:
        			result_string += s[column_index - 2 * i]
        		if column_index < length:
        			result_string += s[column_index]

        		column_index += 2 * numRows - 2
    	return result_string


if __name__ == '__main__':
	s = Solution()
	result = s.convert("AB", 1)
	print result