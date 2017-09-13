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
print(mix(5,5))'''

def init(name,age,city="ChengDu"):
    print('name:',name)
    print('age:',age)
    print("city:",city)
init('bob',20,'XiAn')