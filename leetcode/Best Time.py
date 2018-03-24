#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price,max_profit=float("inf"),0
        for price in prices:
            min_price=min(min_price,price)
            profit=price-min_price
            max_profit=max(profit,max_profit)
        return max_profit