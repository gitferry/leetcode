#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 07/10/2015
'''

import copy
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """

        self.iterator = iterator


    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return copy.deepcopy(self.iterator).next()


    def next(self):
        """
        :rtype: int
        """

        return self.iterator.next()


    def hasNext(self):
        """
        :rtype: bool
        """

        return self.iterator.hasNext()
