#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start,end = 0,len(nums)-1
        while start<end:
            s=nums[start]+nums[end]
            if s==target:
                return [start+1,end+1]
            elif s<target:
                start+=1
            else:
                end-=1