#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'
import collections
class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return len(set(nums)&{v+k for v in nums}) if k>0 else sum(n>1 for n in collections.Counter(nums).values()) if k==0 else 0