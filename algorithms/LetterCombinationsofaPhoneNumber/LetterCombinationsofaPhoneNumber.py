#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 12/08/2015
'''


class Solution:
    # @param {string} digits
    # @return {string[]}
	def letterCombinations(self, digits):
		if not digits:
			return []
		digit_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

		mix_list = []

		self.dfs(digits, digit_map, mix_list, '', 0)

		return mix_list


	def dfs(self, digits, digit_map, mix_list, group, depth):
		if len(group) == len(digits):
			mix_list.append(group)
			return

		for letter in digit_map[digits[depth]]:
			self.dfs(digits, digit_map, mix_list, group + letter, depth + 1)

if __name__ == '__main__':
	s = Solution()
	digits = '7'

	print s.letterCombinations(digits)

