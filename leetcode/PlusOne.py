#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

def plusOne():
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=[1,5,6,8,9]
        num = 0
        print(len(digits))
        for i in range(len(digits)):
    	    num += digits[i] * pow(10, (len(digits)-1-i))
        print([int(i) for i in str(num+1)])

plusOne()