#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 09/10/2015
'''

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.pop(0)


    def peek(self):
        """
        :rtype: int
        """
        return self.queue[0]


    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue):
            return False
        else:
            return True

