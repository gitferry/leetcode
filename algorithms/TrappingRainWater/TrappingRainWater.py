#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 19/08/2015
'''

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        start = 0
        length = len(height)
        container = 0

        while start < length:
            i = start + 1
            temp_container = 0
            temp_heighest = 0
            while i < length:
                if height[i] >= height[start]:
                    container += temp_container
                    start = i
                    break
                else:
                    temp_container += height[start] - height[i]

                if height[i] > temp_heighest:
                    temp_heighest = height[i]

                i += 1

            if i == length:
                if start == length - 1:
                    break
                height[start] = temp_heighest

        return container

if __name__ == '__main__':
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    print s.trap(height)

