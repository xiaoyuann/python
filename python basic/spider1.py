#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora'

import requests
import re

def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''
    
def parsePage(infolist,html):
    try:
        plt = re.findall(r'\"price\"\:\"[\d\.]+\"',html)
        tlt = re.findall(r'\"title\"\:\".*?\"',html)
        for i in range(len(tlt)):
            price = eval(plt[i].split(':')[1]) + '元'
            title = eval(tlt[i].split(":")[1])
            infolist.append([price,title])
    except:
        return ''

def printGoodsList(goodsInfo):
    ptlt = '{:3}\t{:10}\t{:10}'
    print(ptlt.format('序号','价格','商品名称'))
    count = 0
    for info in goodsInfo:
        count = count + 1
        print(ptlt.format(count,info[0],info[1]))


def main():
    goods = '手机'
    pages = 10
    init_url = 'https://s.taobao.com/search?q=' + goods
    goodsInfo = []
    for i in range(pages):
        try:
            url = init_url + '&s=' + str(100 * i)
            html = getHTMLText(url)
            parsePage(goodsInfo,html)
        except:
            continue
    printGoodsList(goodsInfo)    

main()