#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 08/10/2015
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s_list = list(s)
        t_list = list(t)

        return sorted(s_list) == sorted(t_list)


if __name__ == '__main__':
    s = Solution()
    m = 'ba'
    t = 'b'
    print s.isAnagram(m, t)
