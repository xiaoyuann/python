#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import urllib.request,urllib.error
import re
import os

class Spider:
    def __init__(self):
        self.url = 'http://mm.taobao.com/json/request_top_list.htm'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
        self.headers = {'User-Agent':self.user_agent,'Connection':'keep-alive'}#模拟浏览器头
    def getPage(self,pageIndex):
        url = self.url + '?page=' + str(pageIndex)
        try:
            request = urllib.request.Request(url,headers=self.headers)
            response = urllib.request.urlopen(request)
            return response.read().decode('gbk')
        except urllib.error.URLError as e:
            if hasattr(e,'code'):
                print(e.code)
            if hasattr(e,'reason'):
                print(e.reason)
    
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile(r'<div class="list-item".*?<div class="pic s60".*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name".*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>.*?<p>.*?<em>(.*?)</em>.*?',re.S)
        items = re.findall(pattern,str(page))
        contents = []
        for item in items:
            contents.append([item[0],item[1],item[2],item[3],item[4],item[5]])
        return contents

    def getDetailPage(self,infoUrl):
        request = urllib.request.Request(infoUrl,headers=self.headers)
        response = urllib.request.urlopen(request)
        return response.read().decode('gbk')

    def getBrief(self,page):
        pass
    
    def getAllImages(self,page):
        pattern = re.compile(r'<div class="mm-aixiu-content.*?>(.*?)<!--',re.S)
        content = re.match(pattern,page)
        if content is None:
            return None
        patternImage = re.compile(r'src="(.*?)"',re.S)
        imageUrl = re.findall(patternImage,content.group(1))
        return imageUrl

    def saveImgs(self,images,name):
        number = 1
        if images is None:
            return None
        else:
            print('发现 %s 共有 %d 张照骗!' % (name,len(images)))
        for imageUrl in images:
            splitPath = imageUrl.split('.')
            tail = splitPath.pop()
            if len(tail) > 3:
                tail = 'jpg'
            fileName = name + '/' + str(number) + '.' + tail
            self.saveImg(imageUrl,fileName)
            number += 1
    
    def saveIcons(self,iconUrl,name):
        splitPath = iconUrl.split('.')
        tail = splitPath.pop()
        fileName = name + '/icon.' + tail
        self.saveImg(iconUrl,fileName)

    def saveImg(self,imageUrl,fileName):
        s = urllib.request.urlopen(imageUrl)
        image = s.read()
        f = open(fileName,'wb')
        f.write(image)
        print('正在悄悄保存她的图片为%s' % fileName)
        f.close()

    def mkdir(self,path):
        path = path.strip()
        isExist = os.path.exists(path)
        if not isExist:
            print('偷偷新建了名字为%s的文件夹' % path)
            os.makedirs(path)
            return True
        else:
            print('名字为%s的文件夹已经成功创建了呢！' % path)
            return False
    
    def savePageInfo(self,pageIndex):
        contents = self.getContents(pageIndex)
        for item in contents:
            print('发现一位美眉，她叫%s，芳龄%s，她家住%s。' % (item[2],item[3],item[4]))
            print('正在保存%s的个人信息。' % item[2])
            print('哇，惊喜的发现她的个人地址:%s' % item[0])
            detailUrl = 'https:' + item[0]
            detailPage = self.getDetailPage(detailUrl)
            #print(detailPage)
            image = self.getAllImages(detailPage)
            self.mkdir(item[2])
            self.saveIcons('https:' + item[1],item[2])
            for i in range(len(image)):
                self.saveImgs('https' + image[i],item[2])
            

    def savePageInfos(self,start,end):
        for i in range(start,end+1):
            print('正在偷偷寻找第%d个地方，看看妹子们在不在！' % i)
            self.savePageInfo(i)


spider = Spider()
spider.savePageInfos(1,2)            
