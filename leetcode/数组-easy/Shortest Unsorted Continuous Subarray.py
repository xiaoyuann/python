#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len(''.join(('1','0')[a==b] for a,b in zip(sorted(nums),nums)).strip('0'))
        #version2
        '''
        is_same=[a==b for a,b in zip(sorted(nums),nums)]
        return 0 if all(is_same) else len(nums)-is_same.index(False)-is_same[::-1].index(False)
        '''