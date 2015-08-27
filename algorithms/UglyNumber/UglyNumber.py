#!/usr/bin/env python
# coding=utf-8
'''
github: https://github.com/gitferry
author: Fangyu Gai <gaigai508@gmail.com>
date  : 27/08/2015
'''

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return True
        if num <= 0: return False

        prime_factors = self.primes(num)
        print prime_factors

        for factor in prime_factors:
            if factor not in [2, 3, 5]:
                return False

        return True

    def primes(self, num):
        primfac = []
        d = 2
        while d*d <= num:
            while (num % d) == 0:
                primfac.append(d)  # supposing you want multiple factors repeated
                num //= d
            d += 1
        if num > 1:
           primfac.append(num)
        return primfac

if __name__ == '__main__':
    s = Solution()
    num = -2147483648
    print s.isUgly(num)
