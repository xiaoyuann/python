#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        版本一
        return sorted(nums)[len(nums)//2]
        '''
        return [x for x in set(nums) if nums.count(x)>len(nums)//2][0]
