from tkinter import *


def drawTen(event):
    x, y = (event.x, event.y)
    x1, y1 = (event.x - 5), (event.y - 5)
    x2, y2 = (event.x + 5), (event.y + 5)
    canvas.create_line(x, y1, x, y2)
    canvas.create_line(x1, y, x2, y)
    text.set('当前鼠标坐标：{x}，{y}'.format(x=x, y=y))


def clean(event):
    canvas.delete(ALL)


win = Tk()
canvas = Canvas(width=600, height=600, background='white')
canvas.pack()

text = StringVar()
lb = Label(win, textvariable=text)
lb.pack(side=TOP)

canvas.bind("<Button-1>", drawTen)
canvas.bind("<Double-Button-1>", clean)

mainloop()













# from tkinter import *
#
#
# def toRed():
#     w["bg"] = "red"
#
#
# def toYellow():
#     w["bg"] = "yellow"
#
#
# def toBlue():
#     w["bg"] = "blue"
#
#
# def ex():
#     w.quit()
#
#
# w = Tk()
# w.geometry("600x600")
# w.title("窗口颜色")
# m = Menu(w)
# w.config(menu=m)
# m1 = Menu(m)
# #下拉菜单
# m.add_cascade(label="设置", menu=m1)
# m1.add_command(label="黄", command=toYellow)
# m1.add_command(label="蓝", command=toBlue)
# m1.add_command(label="红", command=toRed)
# m1.add_separator()
# m1.add_command(label="退出", command=ex)
# w.mainloop()


# from tkinter import *
# from tkinter.ttk import *
# #将框架（Frame）的共同属性作为默认值，以简化创建过程
# def my_frame(master):
#     w=Frame(master)
#     w.pack(side=TOP,expand=YES,fill=BOTH)
#     return w
# def my_button(master,text,command):
#     w=Button(master,text=text,command=command,width=6)
#     w.pack(side=LEFT,expand=YES,fill=BOTH,padx=2,pady=2)
#     return w
#
# def back(text):
#     if len(text)>0:
#         return text[:-1]
#     else:
#         return text
# def del_sep(text):
#     return text.replace(',','')
#
# def add_sep(text):
#     dot_index = text.find('.')
#     if dot_index > 0:
#         text_head = text[:dot_index]
#         text_tail = text[dot_index:]
#     elif dot_index < 0:
#         text_head = text
#         text_tail = ''
#     else:
#         text_head = ''
#         text_tail = text
#     list_ = [char for char in text_head]
#     length = len(list_)
#     tmp_index = 3
#     while length - tmp_index > 0:
#         list_.insert(length - tmp_index, ',')
#         tmp_index += 3
#     list_.extend(text_tail)
#     new_text = ''
#     for char in list_:
#         new_text += char
#     return new_text
#
# def calc(text):
#     try:
#         if sep_flag.get() == 0:
#             return eval(del_sep(text))
#         else:
#             return add_sep(str(eval(del_sep(text))))
#     except (SyntaxError, ZeroDivisionError, NameError):
#         return 'Error'


# import numpy as np
# import pandas as pd
# from pyecharts import Line
# import time
# import requests
# from bs4 import BeautifulSoup
# from lxml import html
#
#
# class GetAirData:
#     headers = {
#         'Host': 'www.tianqihoubao.com',
#         'Pragma': 'no-cache',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
#         'Cache-Control': 'no-cache',
#         'Connection': 'keep-alive',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
#         'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
#     }
#
#     def getTotalUrl(self, urls, i):
#         url = urls + str("%02d" % i) + '.html'
#         return url
#
#     def openUrl(self, urls, name):
#         for i in range(1, 13):
#             print('正在爬取{place}第{i}个月的数据'.format(place=name, i=i))
#             # time.sleep(0.5)
#             # 把1转换为01
#             url = self.getTotalUrl(urls, i)
#             try:
#                 response = requests.get(url=url, headers=self.headers)
#                 response.raise_for_status()
#                 response.encoding = response.apparent_encoding
#                 s = html.fromstring(response.content)
#             except:
#                 print("解析网页出错")
#                 break
#             soup = BeautifulSoup(response.text, 'html.parser')
#             tr = soup.find_all('tr')
#             # 去除标签栏
#             for j in tr[1:]:
#                 td = j.find_all('td')
#                 Date = td[0].get_text().strip()
#                 Quality_grade = td[1].get_text().strip()
#                 AQI = td[2].get_text().strip()
#                 AQI_rank = td[3].get_text().strip()
#                 PM = td[4].get_text()
#                 fileUrl = 'air_' + name + '.csv'
#                 with open(fileUrl, 'a+', encoding='utf-8-sig') as f:
#                     f.write(Date + ',' + Quality_grade + ',' + AQI + ',' + AQI_rank + ',' + PM + '\n')
#
#         print("数据全部爬取完成")
#
#
# class DrawEcharts:
#     def __init__(self, citys):
#         self.citys = citys
#
#     def draw(self, name):
#         v = []
#         color = ['yellow', 'red', 'blue', 'orange', 'purple']
#         for i in range(5):
#             attr = ["{}".format(str(i) + '月') for i in range(1, 13)]
#             filename = 'air_' + self.citys[i] + '-2018.csv'
#             df = pd.read_csv(filename, header=None, names=["Date", "Quality_grade", "AQI", "AQI_rank", "PM"])
#
#             dom = df[['Date', 'PM']]
#             list1 = []
#             for j in dom['Date']:
#                 time = j.split('-')[1]
#                 list1.append(time)
#             df['month'] = list1
#
#             month_message = df.groupby(['month'])
#             month_com = month_message['PM'].agg(['mean'])
#             month_com.reset_index(inplace=True)
#             month_com_last = month_com.sort_index()
#
#             v1 = np.array(month_com_last['mean'])
#             v1 = ["{}".format(int(i)) for i in v1]
#             v.append(v1)
#
#         line = Line(name, title_pos='center', title_top='0', width=800, height=400)
#         for i in range(len(self.citys)):
#             line.add(self.citys[i], attr, v[i], line_color='red', legend_top='8%')
#         line.render(name+'.html')
#
#
# def main():
#     # 创建爬虫对象
#     getAirData = GetAirData()
#     # 开始爬取各市2018年的天气情况
#     getAirData.openUrl('http://www.tianqihoubao.com/aqi/chengdu-2018', 'chengdu-2018')
#     getAirData.openUrl('http://www.tianqihoubao.com/aqi/beijing-2018', 'beijing-2018')
#     getAirData.openUrl('http://www.tianqihoubao.com/aqi/shenzhen-2018', 'shenzhen-2018')
#     getAirData.openUrl('http://www.tianqihoubao.com/aqi/guangzhou-2018', 'guangzhou-2018')
#     getAirData.openUrl('http://www.tianqihoubao.com/aqi/shanghai-2018', 'shanghai-2018')
#     citys = ['beijing', 'guangzhou', 'shanghai', 'shenzhen', 'chengdu']
#     drawer = DrawEcharts(citys)
#     drawer.draw("2018年北上广深成PM2.5趋势图")
#
#
# if __name__ == "__main__":
#     main()


# v = []
# for i in range(5):
#     filename = 'air_' + citys[i] + '-2018.csv'
#     df = pd.read_csv(filename, header=None, names=["Date", "Quality_grade", "AQI", "AQI_rank", "PM"])
#
#     dom = df[['Date', 'PM']]
#     list1 = []
#     for j in dom['Date']:
#         time = j.split('-')[1]
#         list1.append(time)
#     df['month'] = list1
#
#     month_message = df.groupby(['month'])
#     month_com = month_message['PM'].agg(['mean'])
#     month_com.reset_index(inplace=True)
#     month_com_last = month_com.sort_index()
#
#     v1 = np.array(month_com_last['mean'])
#     v1 = ["{}".format(int(i)) for i in v1]
#     v.append(v1)
#
# attr = ["{}".format(str(i) + '月') for i in range(1, 13)]
#
# line = Line("2018年北上广深成PM2.5趋势图", title_pos='center', title_top='0', width=800, height=400)
# line.add("北京", attr, v[0], line_color='red', legend_top='8%')
# line.add("上海", attr, v[1], line_color='purple', legend_top='8%')
# line.add("广州", attr, v[2], line_color='blue', legend_top='8%')
# line.add("深圳", attr, v[3], line_color='orange', legend_top='8%')
# line.add("成都", attr, v[4], line_color='yellow', legend_top='8%')
# line.render("2018年北上广深成PM2.5趋势图.html")
#
#
#
#
#


#
# print('>>>用户登录<<<')
# with open('user.txt', 'r+', encoding='UTF-8') as f:
#     lines = f.read().splitlines()
#     li = {}
#     for i in lines:
#         li[(i.split(' ')[0])] = (i.split(' ')[1])
# while True:
#     usr = input('用户名:')
#     if usr in li:
#         flag=0
#         while flag < 3:
#             password = input('密码:')
#             if password == li[usr]:
#                 print('Success Login!')
#                 break
#             else:
#                 print("密码错误，重新输入")
#                 flag += 1
#         if flag >= 3:
#             print("登录失败")
#         break
#
#     else:
#         print('账户不存在!')


# import re
#
# def atom_cal(exp):
#     if '*' in exp:
#         a, b = exp.split('*')
#         return str(float(a) * float(b))
#     elif '/' in exp:
#         a, b = exp.split('/')
#         return str(float(a) / float(b))
#
#
# def format_exp(exp):
#     exp = exp.replace('--', '+')
#     exp = exp.replace('+-', '-')
#     exp = exp.replace('-+', '-')
#     exp = exp.replace('++', '+')
#     return exp
#
#
# def mul_div(exp):
#     while True:
#         ret = re.search('\d+(\.\d+)?[*/]-?\d+(\.\d+)?', exp)
#         if ret:
#             atom_exp = ret.group()
#             res = atom_cal(atom_exp)
#             exp = exp.replace(atom_exp, res)
#         else:
#             return exp
#
#
# def add_sub(exp):
#     ret = re.findall('[+-]?\d+(?:\.\d+)?', exp)
#     exp_sum = 0
#     for i in ret:
#         exp_sum += float(i)
#     return exp_sum
#
#
# def cal(exp):
#     exp = mul_div(exp)
#     exp = format_exp(exp)
#     exp_sum = add_sub(exp)
#     return exp_sum
#
#
# def main(exp):
#     exp = exp.replace(' ', '')
#     while True:
#         ret = re.search('\([^()]+\)', exp)
#         if ret:
#             inner_bracket = ret.group()
#             res = str(cal(inner_bracket))
#             exp = exp.replace(inner_bracket, res)
#             exp = format_exp(exp)
#         else:
#             break
#     return cal(exp)
#
#
# s = input("请输入算式：")
# ret = main(s)
# print(ret)


# import random
#
# answer = random.randint(1, 10)
# print('猜数游戏')
# num = input('请输入你猜测的数字(1到10之间的整数\n')
# guess = int(num)
# n = 0
# while n < 4:
#     if guess == answer and n == 0:
#         print('厉害了一次就对了')
#         break
#     if guess < answer:
#         print('太小了')
#     elif guess > answer:
#         print('太大了')
#     elif guess == answer:
#         print('对啦')
#         break
#     num = input('重新输入\n')
#     guess = int(num)
#     n = n + 1
# print('游戏结束')

# from graphics import *
#
# win=GraphWin("求平方根",300,200)
# t1=Text(Point(80,50),"原数")
# t1.setSize(10)
# t1.draw(win)
# input=Entry(Point(200,50),8)
# input.setText("0")
# input.setSize(10)
# input.draw(win)
# output=Text(Point(150,150),"")
# output.draw(win)
# button=Text(Point(150,100),"求平方")
# button.setSize(10)
# button.draw(win)
# Rectangle(Point(100,80),Point(200,120)).draw(win)
# win.getMouse()
# x=eval(input.getText())
# x=x*x
# output.setText(x)
# output.setSize(10)
# button.setText("退出")
# win.getMouse()
# win.close()


# import turtle
#
# turtle.screensize(400, 400)
#
# turtle.penup()
# turtle.goto(0, 0)
# turtle.pendown()
# turtle.pencolor('green')
# turtle.begin_fill()
# turtle.fillcolor('yellow')
# for i in range(4):
#     turtle.forward(80)
#     turtle.left(90)
# turtle.end_fill()
#
# turtle.goto(40, 0)
# turtle.pendown()
# turtle.pensize(2)
# turtle.pencolor('blue')
# turtle.circle(40)
# turtle.penup()


# from tkinter import *
#
# w = Tk()
# c = Canvas(w, width=600, height=600, bg='yellow')
# c.pack()
# rect=c.create_rectangle(500,500,100,100)
# cir=c.create_oval(500,500,100,100)
# w.mainloop()


# import numpy as np
# import matplotlib.pyplot as plt
# import math
#
# x = np.linspace(-10, 10, 2000)
# y = [2 * (math.e) ** (-0.5 * i) * math.sin(2 * i * (math.pi)) for i in x]
# plt.plot(x, y)
# plt.show()


# try:
#     x = float(input("请输入x:"))
#     y = float(input("请输入y:"))
#     if 3 * x - y + 1 < 0:
#         raise NameError('参数错误')
#     import math
#
#     y = math.log(3 * x - y + 1)
#     print('y={Y}'.format(Y=y))
# except ValueError:
#     print("输入错误")
# except NameError:
#     print("3*x-y+1的值小于0")


# with open('a.py', 'r+', encoding='UTF-8') as f:
#     lines = f.readlines()
#     li = []
#     for i in lines:
#         li.append(i.split('#')[0])
#     f.seek(0, 0)
#     f.truncate()
#     for n in li:
#         f.write(n)
#     print(f.read())


# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def cos(self):
#         point = Point(0, 0)
#         l = self.distance(point)
#         return self.x / l
#
#     def distance(self, point):
#         import math
#         return math.fabs(math.sqrt(self.y - point.y) ** 2 - (self.x - point.x) ** 2)
#
#
# A = Point(3, 4)
# B = Point(0, 0)
# print('A到B的距离:{dis}'.format(dis=A.distance(B)))
# print('A的余弦:{cos}'.format(cos=A.cos()))


# import random
#
# A = set()
# B = set()
# for i in range(10):
#     A.add(random.randint(0, 10))
#     B.add(random.randint(0, 10))
#
# print('A:{A}\tB:{B}\t'.format(A=A, B=B))
# print('A长:{A}\tB长:{B}\t'.format(A=len(A), B=len(B)))
# print('A最大:{AMAX}\tA最小:{AMIN}\tB最大:{BMAX}\tB最小:{BMIN}\t'.format(AMAX=max(A), AMIN=min(A), BMAX=max(B), BMIN=min(B)))
# print('并集:{OR}\t交集:{AND}\t差集:{SUB}'.format(OR=A | B, AND=A & B, SUB=A - B))


# name_grade = {'A': 1, 'a': 1, 'B': 2, 'b': 2, 'C': 3, 'c': 3, 'D': 4, 'd': 4, 'E': 5, 'e': 5, 'F': 6, 'f': 6, 'G': 7,
#               'g': 7, 'H': 8, 'h': 8, 'I': 9, 'i': 9, 'J': 10, 'j': 10, 'K': 11, 'k': 11, 'L': 12, 'l': 12, 'M': 13,
#               'm': 13, 'N': 14, 'n': 14, 'O': 15, 'o': 15}
#
# max = -1
# min = 1000
# sum = 0
# for key in name_grade:
#     sum += name_grade[key]
#     if name_grade[key] > max:
#         max = name_grade[key]
#     if name_grade[key] < min:
#         min = name_grade[key]
# average = sum / len(name_grade)
# print('最高:{max}\t最低:{min}\t平均分:{average}'.format(max=max, min=min, average=average))


# def buildList(myList):
#     for i in range(len(myList)):
#         for j in range(len(myList[i])):
#             if i == 0:
#                 myList[i][j] = 1
#             if i == len(myList) - 1:
#                 myList[i][j] = 1
#             if i == j:
#                 myList[i][j] = 1
#             myList[i][0] = 1
#             myList[i][len(myList[i]) - 1] = 1
#
#
# def countZero(myList):
#     sum = 0;
#     for i in range(len(myList)):
#         for j in range(len(myList[i])):
#             if myList[i][j] == 0:
#                 sum += 1
#     return sum
#
#
# myList = [([0] * 6) for i in range(6)]
# buildList(myList)
# for i in myList:
#     print(i)
#
# print(countZero(myList))


# key_value = {'A': 1, 'a': 1, 'B': 2, 'b': 2, 'C': 3, 'c': 3, 'D': 4, 'd': 4, 'E': 5, 'e': 5, 'F': 6, 'f': 6, 'G': 7,
#              'g': 7, 'H': 8, 'h': 8, 'I': 9, 'i': 9, 'J': 10, 'j': 10, 'K': 11, 'k': 11, 'L': 12, 'l': 12, 'M': 13,
#              'm': 13, 'N': 14, 'n': 14, 'O': 15, 'o': 15, 'P': 16, 'p': 16, 'Q': 17, 'q': 17, 'R': 18, 'r': 18, 'S': 19,
#              's': 19, 'T': 20, 't': 20, 'U': 21, 'u': 21, 'V': 22, 'v': 22, 'W': 23, 'w': 23, 'X': 24, 'x': 24, 'Y': 25,
#              'y': 25, 'Z': 26, 'z': 26}
#
# def computer(str):
#     lens = len(str)
#     sum = 0
#     for i in range(lens):
#         sum += key_value[str[i]]
#     return sum
#
#
# strs = input("请输入标志符:")
#
# print(computer(strs))

# i = 65
# j = 1
# while i <= 90:
#     print('{a}{val}{b}{v}{z}'.format(a='\'', val=chr(i), b='\':', v=j, z=','), end="")
#     print('{a}{val}{b}{v}{z}'.format(a='\'', val=chr(i + 32), b='\':', v=j, z=','), end="")
#     i += 1
#     j += 1

# def math(n):
#     return (4 / (4 * n - 3) - 4 / (4 * n - 1))
#
#
# PI = 0
# i = 1
# while 1 / (4 * i - 1) > 0.00001:
#     PI += math(i)
#     i += 1
# print(i)
# print(PI)


# num = int(input("请输出整数："))
# num = num * num if num % 2 != 0 else num ** 3
# print(num)

# num = int(input("请输出整数："))
# if (num % 2 == 0):
#     print(num ** 3)
# else:
#     print(num * num)

# a = list(range(15))
# b = tuple(range(1, 15))
#
# print(a, b, type(a), type(b))
#
# # 产生100以内的奇数
# c = list(range(1, 100))[::2]
# print(c)

# strs = input("输入生日:")
# a = strs.split(",")
# print('我的出生日期是{year}年{month}月{day}日'.format(year=a[0], month=a[1], day=a[2]))
