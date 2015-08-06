#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 06/08/2015
'''

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
	def strStr(self, haystack, needle):
		len_stack, len_needle = len(haystack), len(needle)

		for index in xrange(len_stack - len_needle + 1):
			if needle == haystack[index: index + len_needle]:
				return index

		return -1