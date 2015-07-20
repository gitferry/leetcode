#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 09/06/2015
'''


class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
    	word_map = {}
    	start_index = -1
    	max_len = 0
    	for index in range(len(s)):
    		if word_map.has_key(s[index]) and start_index < word_map.get(s[index]):
    			start_index = word_map.get(s[index])
    		max_len = max(max_len, index - start_index)
    		word_map[s[index]] = index

    	return max_len

if __name__ == '__main__':
	solution = Solution()
	s = "dvdf"
	print solution.lengthOfLongestSubstring(s)