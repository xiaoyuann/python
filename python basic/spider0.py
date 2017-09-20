#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora'


import requests
from bs4 import BeautifulSoup
import bs4

def getHTML(url):
    try:
        kv = {'user-agent':'Mozilla/5.0'}
        r = requests.get(url,headers=kv,timeout=20)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fillList(lists,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            lists.append([tds[0].string,tds[1].string,tds[2].string])

def printList(lists,num):
    tplt = '{0:^10}\t{1:{3}^10}\t{2:^10}'
    print(tplt.format('排名','学校名称','省市',chr(12288)))
    for i in range(num):
        u = lists[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2015_0.html'
    html = getHTML(url)
    fillList(uinfo,html)
    printList(uinfo,100)

main()