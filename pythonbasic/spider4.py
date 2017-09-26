#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import urllib.request,urllib.error
from bs4 import BeautifulSoup

url = 'http://www.qiushibaike.com/hot/page/1'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
headers = {'User-Agent':user_agent,'Connection':'keep-alive'}
try:
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    soup = BeautifulSoup(content,'html.parser')
    L=[]
    M=[]
    for h in soup.find_all('h2'):
    	M.append(h.string)
    for s in soup.find_all('div',{'class':'content'}):
        joke = s.span.get_text('\n','<br/>')
        L.append(joke)
    for j in range(len(L)):
    	print(M[j],L[j],'\n')
except urllib.error.URLError as e:
	if hasattr(e,'code'):
		print(e.code)
	if hasattr(e,'reason'):
		print(e.reason)
