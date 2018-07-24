#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        p = len(nums)
        q = len(nums[0])
        if r*c != p*q:
            return nums

        n = 0
        dst = []
        temp = []
        for mat in nums:
            for i in mat:
                n += 1
                temp.append(i)
                if n == c:
                    dst.append(temp)
                    temp = []
                    n = 0
        return dst