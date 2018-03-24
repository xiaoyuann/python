#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while 1:
            try:
                indexs=nums.index(val)
                nums.pop(indexs)
            except:
                return len(nums)
