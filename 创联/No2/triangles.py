#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'
#版本一
def triangles1(n):
    tri=[[1]]
    for i in range(n):
        tri+=[list(map(lambda x,y:x+y,tri[-1]+[0],[0]+tri[-1]))]
        print(tri[i])


#版本二，使用生成器
def triangles2(n):
    tri=[1]
    while(True):
        yield tri
        tri=[1]+[x+y for x,y in zip(tri[:-1],tri[1:])]+[1]
        n-=1
        if n <= 0:
            break


for i in triangles2(10):
    print(i)