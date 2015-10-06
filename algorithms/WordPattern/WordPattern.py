#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 06/10/2015
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        str_list = str.split(' ')

        str_length = len(str_list)
        pattern_length = len(pattern)

        if str_length != pattern_length:
            return False

        word_map = {}
        for key, word in zip(pattern, str_list):
            if not word_map.has_key(key):
                if word in word_map.values():
                    return False
                word_map[key] = word
            else:
                if word_map[key] != word:
                    return False

        return True

if __name__ == '__main__':
    s = Solution()
    pattern = 'aaa'
    str = 'aa aa aa aa'

    print s.wordPattern(pattern, str)



