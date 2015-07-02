#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 02/02/2015
'''

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
    	expand_s = "#".join("^{}$".format(s))
    	s_length = len(expand_s)
    	print s_length

    	p = [0] * s_length
    	right_bound = before_max_index = 0
    	for i in range(1, s_length-1):
    		if right_bound > i:
    			p[i] = min(p[2*before_max_index - i], right_bound - i)

    		while expand_s[i + p[i] + 1] == expand_s[i - p[i] - 1]:
    			p[i] += 1

    		if i + p[i] > right_bound:
    			right_bound, before_max_index = p[i] + i, i

    	max_length, max_index = max((n, i) for i, n in enumerate(p))
    	return s[(max_index  - max_length)/2: (max_index  + max_length)/2]




if __name__ == '__main__':
	s = Solution()
	longestPalindrome = s.longestPalindrome('abccbac')
	print longestPalindrome
