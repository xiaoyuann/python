#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import requests
from http.cookiejar import CookieJar
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
headers = {'User-Agent':user_agent,'Connection':'keep-alive'}#模拟浏览器头


def getResponseAfterLogin(login_rul):
    uestc_session = requests.Session()
    uestc_session.cookies = CookieJar()
    f = uestc_session.get(login_rul,headers=headers)
    soup = BeautifulSoup(f.text,'html.parser')
    lt = soup.find('input',{'name':'lt'})['value']
    execution = soup.find('input',{'name':'execution'})['value']
    postData = {
        'username':'2016060101007',
        'password':'209081',
        'lt':lt,
        'execution':execution,
        'dllt':'userNamePasswordLogin',
        'rmShown':'1',
        '_eventId':'submit'
    }

    uestc_session.post(login_rul,data=postData,headers=headers)#使用构建好的表单更新cookies
    return uestc_session


def openOtherUrl(other_url,login_rul):
    uestc = getResponseAfterLogin(login_rul)
    return uestc.get(other_url,headers=headers)

def main():
    login_rul = 'http://idas.uestc.edu.cn/authserver/login'
    other_url = 'http://eams.uestc.edu.cn/eams/myPlan.action?_=1506086864459'
    HtmlText = openOtherUrl(other_url,login_rul)
    print(HtmlText.text)


main()
