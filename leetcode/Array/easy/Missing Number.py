#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #版本一
        return (set(range(len(nums)+1))-set(nums)).pop()
        #版本二
        #return len(nums)*(len(nums)+1)//2 - sum(nums)