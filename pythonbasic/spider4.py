#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import urllib.request,urllib.error

url = 'http://www.qiushibaike.com/hot/page/1'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
headers = {'User-Agent':user_agent,'Connection':'keep-alive'}
try:
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    print(response.read().decode())
except urllib.error.URLError as e:
    print(e.code,':',e.reason)
    