#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__Author__ = 'Aurora-Twinkle'

import  requests
from bs4 import BeautifulSoup

LOGIN_URL = 'http://idas.uestc.edu.cn/authserver/login'
get_url = 'http://eams.uestc.edu.cn/eams/courseTableForStd.action?_=1506058028934'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
headers = {'User-Agent':user_agent,'Connection':'keep-alive'}

uestc_session = requests.Session()
f = uestc_session.get(LOGIN_URL,headers=headers)
soup = BeautifulSoup(f.text,'html.parser')
lt = soup.find('input',{'name':'lt'})['value']
execution = soup.find('input',{'name':'execution'})['value']

values = {
    'username':'2016060101007',
    'password':'',
    'lt':lt,
    'execution':execution,
    '_eventId':'submit',
    'rmShown':'1',
    'dllt':'userNamePasswordLogin'
    }

uestc_session.post(LOGIN_URL,data=values,headers=headers)
f = uestc_session.get(get_url,headers=headers)
print(f.text)