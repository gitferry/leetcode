#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 24/07/2015
'''

class Solution:
    # @param {integer} n
    # @return {string[]}
	def generateParenthesis(self, n):
		collection = []
		self.generate(collection, '', n, n)
		return collection

	# @param {string[]} collection: all the parentheses string
	# @param {string} current: current parenthes string
	# @param {integer} left: number of '(' to be placed
	# @param {integer} right: number of '(' to be placed
	def generate(self, collection, current, left, right):
		if left <= 0 and right <= 0:
				collection.append(current)
		else:
			if left > 0:
				self.generate(collection, current + '(', left - 1, right)
			if left < right:
				self.generate(collection, current + ')', left, right - 1)
