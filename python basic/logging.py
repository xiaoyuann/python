#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__Author__ = 'Aurora-Twinkle'

import urllib.request,urllib.parse,urllib.error
import http.cookiejar

LOGIN_URL = 'http://www.jobbole.com/wp-admin/admin-ajax.php '
get_url = 'http://top.jobbole.com/37578/?utm_source=www.jobbole.com&utm_medium=sidebar-top-news'

values = {'action':'user_login','user_login':'userr1','user_pass':'4dANH$4)3)vxrj#B'}
postdata = urllib.parse.urlencode(values).encode()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
headers = {'User-Agent':user_agent,'Connection':'keep-alive'}

cookie_filename = 'cookie0.txt'
cookie = http.cookiejar.MozillaCookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(LOGIN_URL,postdata,headers=headers)
try:
    response = opener.open(request)
    page = response.read().decode()
except urllib.error.HTTPError as e:
    print(e.code,':',e.reason)
except urllib.error.URLError as e:
    print(e.code,':',e.reason)

cookie.save(filename=cookie_filename,ignore_discard=True,ignore_expires=True)
print(cookie)
for item in cookie:
    print('name = '+item.name)
    print('value = '+item.value)

get_request = urllib.request.Request(get_url,headers=headers)
get_response = opener.open(get_request)
print(get_response.read().decode())