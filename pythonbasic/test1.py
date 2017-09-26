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
        pattern = re.compile(r'<div class="list-item".*?<div class="pic s60".*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name".*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>.*?<p>.*?<em>(.*?)</em>.*?',re.S)
        items = re.findall(pattern,page)
        contents = []
        for item in items:
            print(item[1])

spider = Spider()
spider.getContents(1)
