#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 19/07/2015
'''

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
    	height_number = len(height)
    	max_container = 0

    	start_pointer = 0
    	end_pointer = height_number - 1
    	while start_pointer < end_pointer:
    		container = (end_pointer - start_pointer) * \
    		min(height[start_pointer], height[end_pointer])
    		max_container = max(max_container, container)

    		if height[start_pointer] < height[end_pointer]:
    			start_pointer += 1
    		elif height[start_pointer] > height[end_pointer]:
    			end_pointer -= 1
    		else:
    			start_pointer += 1
    			end_pointer -= 1

    	return max_container


if __name__ == '__main__':
	s = Solution()
	height = []
	print s.maxArea()
