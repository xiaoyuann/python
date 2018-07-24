#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

class Solution:
    def generate(self, numRows):
        s = [[1]]
        for i in range(1, numRows):
            s += [list(map(lambda x, y: x+y, s[-1] + [0], [0] + s[-1]))]
        return s[:numRows]
        