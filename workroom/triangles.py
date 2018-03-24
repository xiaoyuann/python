#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

def triangles(n):
    tri=[[1]]
    for i in range(n):
        tri+=[list(map(lambda x,y:x+y,tri[-1]+[0],[0]+tri[-1]))]
        print(tri[i])

triangles(10)