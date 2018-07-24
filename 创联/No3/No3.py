#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import random

def func1():#被三不能被五整除，取出下标为偶数的数，逆序
    nums=[x for x in range(1,10001) if x % 3 == 0 and x % 5 != 0]
    nums1=[nums[x] for x in range(len(nums)) if x%2 == 0]
    nums.reverse()
    print(nums)

def func2():#统计数字与去重
    a=[random.randint(0,100) for _ in range(500)]
    a1=set(a)
    for a2 in a1:
        print(a2,":",a.count(a2))
    a=set(a)
