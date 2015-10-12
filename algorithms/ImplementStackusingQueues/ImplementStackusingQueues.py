#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 12/10/2015
'''

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.insert(0, x)


    def pop(self):
        """
        :rtype: nothing
        """
        self.stack.pop(0)


    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]


    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack):
            return False
        else:
            return True
