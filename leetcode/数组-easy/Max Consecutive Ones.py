#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=''.join(map(str,nums)).split('0')
        return max(map(len,a))
        #version 2
        '''
        count,result=0,0
        for num in nums:
            if num==1:
                count+=1
                result=max(result,count)
            else:
                count=0
        return max(result,count)
            '''