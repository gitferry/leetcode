#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 21/07/2015
'''

class Solution:
    # @param {string} s
    # @return {boolean}
	def isValid(self, s):
		stash = []

		for char in s:
			if not stash:
				stash.append(char)
			else:
				if stash[-1] == '(':
					if char == ')':
						stash.pop()
					else:
						stash.append(char)
				elif stash[-1] == '[':
					if char == ']':
						stash.pop()
					else:
						stash.append(char)
				elif stash[-1] == '{':
					if char == '}':
						stash.pop()
					else:
						stash.append(char)

		if stash:
			return False
		else:
			return True



if __name__ == '__main__':
	s = Solution()
	print s.isValid("([)")

