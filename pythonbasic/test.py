import urllib.request, urllib.parse, urllib.error
import http.cookiejar

cookie_filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
cookie.load(cookie_filename, ignore_discard=True, ignore_expires=True)
print(cookie)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

get_url = 'http://eams.uestc.edu.cn/eams/home!childmenus.action?menu.id=844'  # 利用cookie请求访问另一个网址
get_request = urllib.request.Request(get_url)
get_response = opener.open(get_request)
print(get_response.read().decode())