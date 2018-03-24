#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return len(nums)
        else:
            j=0
            for i in list(range(len(nums)))[1:len(nums)]:
                if nums[j]!=nums[i]:
                    j+=1
                    nums[j]=nums[i]
            return j+1
                