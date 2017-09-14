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
print(L2)'''

from PIL import Image
im = Image.open('test.png')
print(im.format, im.size, im.mode)