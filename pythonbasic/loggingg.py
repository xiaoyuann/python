#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__Author__ = 'Aurora-Twinkle'

import requests
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup

class WHUHelper(object):
    __loginuri='http://idas.uestc.edu.cn/authserver/login'
    __logindo='http://eams.uestc.edu.cn/eams/myPlan.action?_=1506086864459'
    def __init__(self,name='',password=''):
        if not isinstance(name,str):
            raise TypeError('请输入字符串')
        else:
            self.name=name
        if isinstance(password,int):
            self.password=str(password)
        elif isinstance(password, str):
            self.password=password
        else:
            raise TypeError('请输入字符串')
    def __getResponseAfterLogin(self):
        #模拟一个浏览器头
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
        #保持Cookie不变，然后再次访问这个页面
        s=requests.Session()
        #CookieJar可以帮我们自动处理Cookie
        s.cookies=CookieJar()
        #得到一个Response对象，但是此时还没有登录
        r=s.get(self.__loginuri,headers=header)
        #得到postdata应该有的lt#这里使用BeautifulSoup对象来解析XML
        dic={}
        lt=BeautifulSoup(r.text,'html.parser')
        for line in lt.form.findAll('input'):
            if(line.attrs['name']!=None):
                dic[line.attrs['name']]=line.attrs['value']
        params={
            'username':self.name,
            'password':self.password,
            'dllt':'userNamePasswordLogin',
            'lt':dic['lt'],
            'execution':dic['execution'],
            '_eventId':dic['_eventId'],
            'rmShown':dic['rmShown']}
        #使用构建好的PostData重新登录,以更新Cookie
        r=s.post(self.__loginuri, data=params,headers=header)
        return s
    def getHtmlOfPerson(self):
        s=self.__getResponseAfterLogin()
        personUri='http://eams.uestc.edu.cn/eams/home!childmenus.action?menu.id=844'
        r=s.get(personUri)
        return r.text
    '''def getPersonInfor(self):
        s=self.__getResponseAfterLogin()
        bs=BeautifulSoup(self.__getHtmlOfPerson(),'html.parser')
        dic={}
        #得到基本信息get方式的访问URL网站
        jbxxUri=self.__logindo+bs.find('a',{'text':'基本信息'}).attrs['url']
        r=s.get(jbxxUri)
        bs=BeautifulSoup(r.text,'html.parser')
        dic['学号']=bs.find('input',{'name':'jbxx.xh'}).attrs['value']
        dic['姓名']=bs.find('input',{'name':'jbxx.xm'}).attrs['value']
        return dic
    def getClassInfo(self):
        #初始化课表
        classInfo=[]
        classTitle=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
        for i in range(13):
            singleclass=[]
            for j in range(7):
                singleclass.append('')
            classInfo.append(singleclass)
        #首先得到登陆后的request
        s=self.__getResponseAfterLogin()
        bs=BeautifulSoup(self.__getHtmlOfPerson(),'html.parser')
        jbxxkb=self.__logindo+bs.find('a',{'text':'我的课表'}).attrs['url']
        r=s.get(jbxxkb)
        bs=BeautifulSoup(r.text,'html.parser')
        #得到每天十三节课
        trs=bs.find('table',{'class':'table_con'}).findAll('tr',{'class':'t_con'})
        for i in range(len(trs)):
            tds=trs[i].findAll('td')
            #表示星期几
            j=0
            for td in tds: 
                if td.find('b')!=None:
                    continue#beautifulsoup会把 解析为\a0，所以这里需要先转码，然后在编码
                classInfo[i][j]=str(td.get_text()).encode('gbk','ignore').decode('gbk')
                j=j+1
        classInfo.insert(0, classTitle)        
        return classInfo'''

a = WHUHelper('2016060101007','')
print(a.getHtmlOfPerson())