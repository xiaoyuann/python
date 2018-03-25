#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=len(nums)
        if l==0:
            return 0
        elif target in nums:
            return nums.index(target)
        else:
            start=0
            end=l-1
            while start<=end:
                mid=(start+end)/2
                if nums[mid]>=target:
                    end=mid-1
                else:
                    start=mid+1
            return start

'''一行解决
return len([x for x in nums if x<target])
'''
