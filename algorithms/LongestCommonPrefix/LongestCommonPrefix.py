#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 07/12/2015
'''

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
    	if len(strs) == 0:
    		return ""

    	strs = sorted(strs, key=len)

    	base_string = strs[0]

    	for j, char_item in enumerate(base_string):
    		for i, string_item in enumerate(strs[1:]):
    			if char_item != string_item[j]:
    				return base_string[0: j]

    	return base_string


if __name__ == '__main__':
	s = Solution()
	strings = ['a']
	print s.longestCommonPrefix(strings)


