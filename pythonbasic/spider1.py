#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#爬取淘宝手机信息

__author__ = 'Aurora-Twinkle'

import requests
import re
import xlwt


def getHTMLText(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}#模拟浏览器发起访问
        r = requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()#检测是否成功响应服务器
        r.encoding = r.apparent_encoding
        print(r.request.headers)
        return r.text
    except:
        return ''
    
def parsePage(infolist,html):
    try:
        f = xlwt.Workbook()#创建表格存入爬取数据
        sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True)
        plt = re.findall(r'\"price\"\:\"[\d\.]+\"',html)#使用正则匹配所需信息
        tlt = re.findall(r'\"title\"\:\".*?\"',html)
        for i in range(len(tlt)):
            price = eval(plt[i].split(':')[1]) + '元'
            title = eval(tlt[i].split(":")[1])
            infolist.append([price,title])
        for j in range(len(infolist)):
            sheet1.write(j,1,infolist[j][0])
            sheet1.write(j,2,infolist[j][1])
        f.save('test.xls')
    except:
        return ''

def printGoodsList(goodsInfo):
    ptlt = '{:3}\t{:10}\t{:10}'#格式化输出信息
    print(ptlt.format('序号','价格','商品名称'))
    count = 0
    for info in goodsInfo:
        count = count + 1
        print(ptlt.format(count,info[0],info[1]))


def main():
    goods = '手机'
    pages = 3#访问网页数
    init_url = 'https://s.taobao.com/search?q=' + goods
    goodsInfo = []
    for i in range(pages):
        try:
            url = init_url + '&s=' + str(44 * i)
            html = getHTMLText(url)
            parsePage(goodsInfo,html)
        except:
            continue
    printGoodsList(goodsInfo)    

main()