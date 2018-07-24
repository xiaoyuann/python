#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import requests
import os
import time
from lxml import html

class MeiZiTu(object):
    def __init__(self):
        self.urls = []#用来存储专题图片链接

    #模拟浏览器头，对抗反爬虫
    def getHeaders(self,referer):
        headers = {
            'Host': 'i.meizitu.net',
            'Pragma': 'no-cache',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
            'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
            'Referer': '{}'.format(referer)
        }
        return headers

    def getUrl(self,pageIndex):
        url = 'http://www.mzitu.com/page/' + str(pageIndex)#首页链接
        try:
            response = requests.get(url)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            s = html.fromstring(response.content)
            for i in s.xpath('//ul[@id="pins"]/li/a/@href'):
                self.urls.append(i)#将专题链接存入列表
        except:
            return None

    def getPhotos(self,url):
        s = html.fromstring(requests.get(url).content)
        total = s.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()')[0]#专题图片总数
        title = s.xpath('//h2[@class="main-title"]/text()')[0]
        fileName = '【{}P】{}'.format(total,title)#文件夹名字
        os.mkdir(fileName)
        n = 1
        for i in range(int(total)):
            try:
                jpgUrl = '{}/{}'.format(url,i+1)
                ss = html.fromstring(requests.get(jpgUrl).content)
                jpgUrls = ss.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
                jpgName = '%s/%s/%s.jpg' % (os.path.abspath('.'),fileName,n)
                with open(jpgName,'wb') as jpg:
                    print("正在偷偷保存相册：%s 第%s张" % (fileName,n))
                    jpg.write(requests.get(jpgUrls,headers=self.getHeaders(jpgUrls)).content)
                    jpg.close()
                n += 1
            except:
                return None
    def start(self,number):
        self.getUrl(number)
        for e in self.urls:
            self.getPhotos(e)
            time.sleep(2)    

spider = MeiZiTu()
spider.start(1)