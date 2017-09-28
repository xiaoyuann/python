#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import requests
import os
import time
from lxml import html

def header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers

def getPage(pageIndex):
    url = 'http://www.mzitu.com/page/' + str(pageIndex)
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        s = html.fromstring(response.text)
        urls = []
        for i in s.xpath('//ul[@id="pins"]/li/a/@href'):
            urls.append(i)
            print(i)
        return urls
    except:
        return None

def getJpgUrl(url):
    se = html.fromstring(requests.get(url).content)
    total = se.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()')[0]
    title = se.xpath('//h2[@class="main-title"]/text()')[0]
    dirName = '【{}P】{}'.format(total,title)
    os.mkdir(dirName)
    n = 1
    for i in range(int(total)):
        try:
            urll = '{}/{}'.format(url,i+1)
            set = html.fromstring(requests.get(urll).content)
            jpgUrl = set.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
            filename = '%s/%s/%s.jpg' % (os.path.abspath('.'), dirName, n)
            print('开始下载图片:%s 第%s张' % (dirName, n))
            with open(filename,'wb+') as jpg:
                jpg.write(requests.get(jpgUrl,header=header(jpgUrl)).content)
                n += 1
        except:
            return None

p = getPage(1)
for e in p:
    print(e)
    getJpgUrl(e)
    
        
    


