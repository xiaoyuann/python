#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Aurora-Twinkle'

import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

class Time(object):
    
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second
    
    def __str__(self):
        return '(Time: %s:%s:%s)' % (self.hour,self.minute,self.second)
    __repr__ = __str__

    def __add__(self,other):
        return '(Time:%s:%s:%s)' % (self.hour+other.hour,self.minute+other.minute,self.second+other.second)

    def __sub__(self,other):
        return '(Time:%s:%s:%s)' % (self.hour-other.hour,self.minute-other.minute,self.second-other.second)

    def __le__(self,other):
        if self.hour<other.hour:
            return True
        elif self.hour==other.hour:
            if self.minute<other.minute:
                return True
            elif self.hour==other.hour:
                if self.second<other.second:
                    return True
                elif self.second==other.second:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    

class Date(object):
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    
    def __str__(self):
        return '(Date:%s/%s/%s)' % (self.year,self.month,self.day)
    __repr__ = __str__

    def __add__(self,other):
        return '(Date:%s/%s/%s)' % (self.year+other.year,self.month+other.month,self.day+other.day)

    def __sub__(self,other):
        return '(Date:%s/%s/%s)' % (self.year-other.year,self.month-other.month,self.day-other.day)


class Datetime(Time,Date):
    def __init__(self,hour,minute,second,year,month,day):
        Time.__init__(self,hour,minute,second)
        Date.__init__(self,year,month,day)
    
    def __str__(self):
        return '(time:%s/%s/%s %s:%s:%s)' % (self.year,self.month,self.day,self.hour,self.minute,self.second)
    __repr__ = __str__
    
    def __add__(self,other):
        return '(time:%s/%s/%s %s:%s:%s)' % (self.year+other.year,self.month+other.month,self.day+other.day,self.hour+other.hour,self.minute+other.minute,self.second+other.second)

    def __sub__(self,other):
        return '(time:%s/%s/%s %s:%s:%s)' % (self.year-other.year,self.month-other.month,self.day-other.day,self.hour-other.hour,self.minute-other.minute,self.second-other.second)

    def date(self):
        print('(Date:%s/%s/%s)' % (self.year,self.month,self.day))

    def time(self):
        print('(Time: %s:%s:%s)' % (self.hour,self.minute,self.second))


t=Time(1,1,1)
t1=Time(1,1,0)
d=Date(2018,3,25)
d1=Date(2004,2,5)
dt=Datetime(1,1,1,2018,3,25)
dt1=Datetime(1,1,1,2019,3,25)
dt.date()
dt1.time()