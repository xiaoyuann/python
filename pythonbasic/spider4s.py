#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import urllib.request,urllib.error
from bs4 import BeautifulSoup

class QSBK(object):
	"""docstring for QSBK"""
	def __init__(self):
		self.pageIndex = 1
		self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
		self.headers = {'User-Agent':self.user_agent,'Connection':'keep-alive'}
		self.stories = []
		self.enable = False
	def getPage(self,pageIndex):
		try:
			url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
			request = urllib.request.Request(url,headers = self.headers)
			response = urllib.request.urlopen(request)
			content = response.read().decode('utf-8')
			soup = BeautifulSoup(content,'html.parser')
			return soup
		except urllib.error.URLError as e:
			print('服务器响应失败\n')
			if hasattr(e,'code'):
				print(e.code)
			if hasattr(e,'reason'):
				print(e.reason)

	def getPageItem(self,pageIndex):
		soup = self.getPage(pageIndex)
		if not soup:
			print('页面加载失败')
			return None
		authors = []
		jokes = []
		pageStories = []
		for s in soup.find_all('div',{'class':'content'}):
			jokes.append(s.span.get_text('\n','<br/>'))
		for h in soup.find_all('h2'):
			authors.append(h.string)
		for i in range(len(authors)):
			pageStories.append([authors[i],jokes[i]])
		return pageStories

	def loadPage(self):
		if self.enable == True:
			if len(self.stories) < 2:
				pageStories = self.getPageItem(self.pageIndex)
				if pageStories:
					self.stories.append(pageStories)
					self.pageIndex += 1

	def getOneStory(self,pageStories,page):
		for story in pageStories:
			#inputs = input()
			self.loadPage()
			# if inputs == 'Esc':
			# 	self.enable = False
			# 	return None
			for i in range(100):
				print('第%d页\t发布人:%s\t正文:%s\n' % (page,story[i][0],story[i][1]))

	def start(self):
		print('正在读取糗事百科，按回车查看新段子，Esc退出')
		self.enable = True
		self.loadPage()
		nowPage = 0
		while  self.enable:
			if len(self.stories)>0:
				pageStories = self.stories[0]
				nowPage += 1
				del self.stories[0]
				self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()