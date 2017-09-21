#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''s4=input()
s5=input()
s1=int(s4)
s2=int(s5)
s3=((s2-s1)/s1)*100
print('小明的成绩提高了%.2f%%' % s3)
novel=["七界传说","斗破苍穹"]
print(novel[1])
novel.insert(1,'大主宰')
print(novel[2])
novel.pop(1)
print(novel)
print(len(novel))
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
sum=0
for s in range(101):
	sum=sum+s
	print(sum)
print(sum)
L = ['Bart', 'Lisa', 'Adam']
for h in L:
	print('hello,%s' % h)
do={'bob':12,'lucy':15,'tom':16}
print(do['bob'])
d=do.get('bob',-1)
print(d)
s=set([1,2,3,4])
print(s)
def mix(x,n=3):
    s=1
    while n>0:
        s=s*x
        n=n-1
    return s
print(mix(5,5))

def init(name,age,city="ChengDu"):
    print('name:',name)
    print('age:',age)
    print("city:",city)
init('bob',20,'XiAn')

def append(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
print(append())
print(append())
print(append())

def person(name,phone,**kw):
    print('name:',name,'phone:','other:',kw)
person('bob',12586,number='3568+')



def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
def fact(n):
    return fact_iter(n, 1)
print(fact(5))

def hanoi(n,A,B,C):
    if n==1:
        print(A,"--->",C)
    else:
        hanoi(n-1,A,C,B)
        hanoi(1,A,B,C)
        hanoi(n-1,B,A,C)

hanoi(10,'A','B','C')

from collections import Iterable
print(isinstance('ishjdsvn',Iterable))
for k in 'kfnskjnf':
    print(k)

l=[1,2,4,54]
print(l[-2:-1])

l=[x*x for x in range(1,10001) if x%2 == 0]
print(l)

print([m + n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')])

def tri():
    b=[1]
    while True:
        yield b
        b=[1]+[sum(b[i:i+2]) for i in range(len(b)-1)]+[1]

n=0
for t in tri():
  print(t)
  n+=1
  if n>10:
     break

L1=['adam','LISA','barT']
def normalize(name):
   return name[0].upper()+name[1:].lower()
print(list(map(normalize,L1)))

l=[1,2,5,98,6]
print(l[::2])

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score,reverse=True)
print(L2)

from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)

import re  
s = "[lol]你好，帮我把这些markup清掉，[smile]。谢谢！"
print (re.sub('你.*?这', '', s))

import os
print(os.environ)

from datetime import datetime
now=datetime.now()
print(now)

from urllib import request

with request.urlopen('http://www.81js.com/') as f:
    data = f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'%(k,v))
    print('Data:',data.decode('utf-8'))

from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('/Library/Fonts/Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# 设置窗口标题:
app.master.title()
# 主消息循环:
app.mainloop()

import socket
sina=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sina.connect(('www.sina.com.cn',80))
sina.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    # 每次最多接收1k字节:
    d = sina.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
sina.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)

import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')
logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warning('this is a warning message')

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

import requests

response = requests.get('http://www.baidu.com')
print(response.status_code)
print(response.text)
print(response.encoding)
print(response.apparent_encoding)
response.encoding = response.apparent_encoding
print(response.text)

import requests

def getHTML(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '出现异常'

url='http://www.sina.com'
print(getHTML(url))

import  requests

try:
    kv = {'user-agent':'Mozilla/5.0'}
    url = 'https://item.jd.com/5005885.html'
    r = requests.get(url,timeout=10,headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:5000])
    print(r.request.headers)
except:
    print('爬取失败')

import requests
import os
url = 'https://telerik-fiddler.s3.amazonaws.com/fiddler/FiddlerSetup.exe'
root = 'E://mov//'
path = root+url.split('/')[-1]
kv = {'user-agent':'Mozilla/5.0'}
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url,headers=kv)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('保存成功')
    else:
        print("文件已存在")
except:
    print('爬取失败')'''



import urllib.request,urllib.parse,urllib.error
import http.cookiejar

LOG_URL = 'http://idas.uestc.edu.cn/authserver/login'
values = {'username':'2016060101007','password':'209081'}
postdata = urllib.parse.urlencode(values).encode()
user_agent = r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
headers = {'User-Agent':user_agent,'Connection':'keep-alive'}

cookie_filename = 'cookie.txt'

cookie = http.cookiejar.MozillaCookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(LOG_URL,postdata,headers)
try:
    response = opener.open(request)
    page = response.read().decode()
except urllib.error.URLError as e:
    print(e.code,':',e.reason)

cookie.save(filename=cookie_filename,ignore_discard=True,ignore_expires=True)
print(cookie)
for item in cookie:
    print('name = ' + item.name)
    print('value = ' + item.value)


get_request = urllib.request.Request(get_url,headers)
get_response = opener.open(get_request)
print(get_response.read().decode())