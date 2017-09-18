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
loop.run_forever()'''

import urllib.request
import threading
import xlrd
import time
import random
#初始数据
######################
data_file = 'data.xlsx'
data_file = '162四六级考生安排161205.xlsx'
out_file = 'out.csv'
xff = random.randint(1,999999)
max_rows = 0
threading_max = 1000
threads = []
error_num = []
now = 1
now_write = 1
lock = threading.Lock()
sync_with_num = False
start_time = time.time()
######################

def query_function():
    global rsh
    global xff
    global now
    global now_write
    global rows
    global max_rows
    global sync_with_num
    global error_num
    while True:
        #print(threading.current_thread().name,1)
        lock.acquire()
        if now >= (max_rows or rows):
            break
            #print(now)

        now_query = now
        now += 1
        lock.release()
        zkzh = rsh.cell_value(now_query, column_data[0]).replace(' ','')
        xm = rsh.cell_value(now_query, column_data[1]).replace(' ','')
        num = rsh.cell_value(now_query, column_data[2]).replace(' ','')
        #print(threading.current_thread().name,2)
        xff_tmp, total_score = query_data(zkzh, xm, xff, 0)
        lock.acquire()
        xff = xff_tmp
        if sync_with_num:
            lock.release()
            while now_query != now_write:
                #print(threading.current_thread().name,3)
               pass

        fp.write('%s,%s,%s,%s\n' % (zkzh, xm, num, total_score))
        print('%d/%d,%s 当前已完成:%.2f%%' % (now_write, rows - 1, xm, now_write * 100 / (rows - 1)))
        now_write += 1
        if not sync_with_num:
            lock.release()
    lock.release()
def query_data(zkzh, xm, xff, err_num):
    #查询
    url = 'http://www.chsi.com.cn/cet/query?'
    query = {'zkzh': zkzh, 'xm': xm}
    headers = {'Referer':'http://www.chsi.com.cn/cet/','X-Forwarded-For':'127.0.0.' + str(xff)}
    query = urllib.parse.urlencode(query)
    req = urllib.request.Request(url + query,None,headers)
    for i in range(10):
        try:
            text = urllib.request.urlopen(req).read().decode('utf8')
            break
        except Exception as e:
            if i:
                print('正在进行第' + str(i) + '次重试')
            print ('哎呀，你的网络炸了呢',e)
            if i == 9:
                print ('人家才不会和网络差的人一起玩呢，哼～～～～～～～～～～～～～～～～～～～～')
                lock.acquire()
                error_num.append((xm, zkzh, str(e)))
                lock.release()
                exit()
        
    #处理数据
    search_text = ['<span class="colorRed">', '</span>']
    total_score_start = text.find(search_text[0])
    total_score_start += len(search_text[0])
    total_score_end = text.find(search_text[1], total_score_start)
    try:
        total_score = str(int(text[total_score_start:total_score_end]))
        ret = (xff, total_score)
    except Exception as e:
        print(xm + '查询出错了呢,人家再帮你试一次吧')
        if err_num < 3:
            ret = query_data(zkzh, xm, xff + 1, err_num + 1)
        else:
            print('连续错误那么多次，人家不查这人了，哼～～～～～～～～～～～～～～～～～')
            lock.acquire()
            error_num.append((xm, zkzh, str(e)))
            lock.release()
            return (0, 'error')
    return ret


print('读取表格数据...')
try:
    rbook = xlrd.open_workbook(data_file)
except FileNotFoundError as e:
    print ('连文件都没有，你让人家怎么查嘛，根本找不到' + data_file + '的说')
    exit()

rsh = rbook.sheet_by_index(0)
rows = rsh.nrows
column = rsh.ncols
header = rsh.row_values(0)
column_data = [None] * 3
for i in range(column):
    header_text = str(header[i])
    if '准考证' in header_text:
        column_data[0] = i
    elif '姓名' in header_text:
        column_data[1] = i
    elif '学号' in header_text:
        column_data[2] = i
print('读取完成...')

print('正在进行查询...')
fp = open(out_file,'w')
fp.write('准考证号,姓名,学号,四级成绩\n')
while now < (max_rows or rows):
    if len(threads) <= min(threading_max, rows - now):
        threads.append(threading.Thread(target=query_function))
        threads[len(threads) - 1].start()
for i in threads:
    i.join()

    #else:
        #break
print("共查询了%d条数据,失败%d条,用时%ds" % (now, len(error_num), time.time() - start_time))
if error_num:
    print("失败名单：")
    for i in error_num:
        print("%s:%s %s" % i)