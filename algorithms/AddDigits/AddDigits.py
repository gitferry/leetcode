#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 05/10/2015
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        num_string = str(num)
        if len(num_string) == 1:
            return num

        digits_sum = sum(int(c) for c in num_string)
        return self.addDigits(digits_sum)

if __name__ == '__main__':
    s = Solution()
    num = 38
    print s.addDigits(num)
