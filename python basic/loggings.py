#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__Author__ = 'Aurora-Twinkle'

import  requests
from bs4 import BeautifulSoup

LOGIN_URL = 'http://idas.uestc.edu.cn/authserver/login'
get_url = 'http://eams.uestc.edu.cn/eams/home!childmenus.action?menu.id=844'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
headers = {'User-Agent':user_agent,'Connection':'keep-alive'}
uestc_session = requests.Session()
f = uestc_session.get(LOGIN_URL,headers=headers)
soup = BeautifulSoup(f.content,'html.parser')
lt = soup.find('input',{'name':'lt'})['value']
print(lt)
values = {
    'username':'2016060101007',
    'password':'',
    'lt':lt
    }
uestc_session.post(url,data=values,headers=headers)
f = uestc_session.get(get_url,headers=headers)
print(f.content.decode('utf-8'))