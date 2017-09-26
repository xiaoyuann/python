#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import urllib.request,urllib.error
import re
import os
class Spider:
    def __init__(self):
        self.url = 'http://mm.taobao.com/json/request_top_list.htm'
    
    def getPage(self,pageIndex):
        url = self.url + '?page=' + str(pageIndex)
        print(url)
        try:
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            return response.read().decode('gbk')
        except urllib.error.URLError as e:
            if hasattr(e,'code'):
                print(e.code)
            if hasattr(e,'reason'):
                print(e.reason)
    
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile(r'<div class="list-item".*?<div class="pic s60".*?<a href="(.*?)".*?<img src="(.*?).*?<a class="lady-name".*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>.*?<p>.*?<em>(.*?)</em>.*?',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            contents.append([item[0],item[1],item[2],item[3],item[4],item[5]])
        return contents

    def 
MM = Spider()
MM.getContents(1)