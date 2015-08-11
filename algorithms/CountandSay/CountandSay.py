#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 11/08/2015
'''

class Solution:
    # @param {integer} n
    # @return {string}
	def countAndSay(self, n):
		if n == 1: return '1'
		n -= 1
		original_string = '1'

		for i in range(n):
			length = len(original_string)
			new_string = ''
			count = 1
			j = 0
			while j < length:
				while j < length - 1 and original_string[j] == original_string[j + 1]:
					j += 1
					count += 1
				new_string += str(count) + original_string[j]
				count = 1
				j += 1
			original_string = new_string

		return original_string


if __name__ == '__main__':
	s = Solution()
	n = 3
	print s.countAndSay(n)
