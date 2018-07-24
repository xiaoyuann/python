#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsub,temp=nums[0],0
        for i in nums:
            temp = max([i,i+temp])
            maxsub = max(maxsub,temp)
        return maxsub
        