#! /usr/bin/python
#coding=utf-8
import datetime
from datetime import timedelta
from datetime import tzinfo
import os
import re
import socket
import sys
import time
import urllib2
import copy 
    
class GMT8(tzinfo):
    delta = timedelta(hours=8)
    def utcoffset(self, dt):
        return self.delta
    def tzname(self, dt):
        return "GMT+8"
    def dst(self, dt):
        return self.delta

class GMT(tzinfo):
    delta = timedelta(0)
    def utcoffset(self, dt):
        return self.delta
    def tzname(self, dt):
        return "GMT+0"
    def dst(self, dt):
        return self.delta 

def getlocaldate(time=0):
 
    from_tzinfo =    GMT()#格林威治时区，0时区
    local_tzinfo =  GMT8()#本地时区，+8区

    gmt_time = datetime.datetime.utcnow()
    gmt_time = gmt_time.replace(tzinfo=from_tzinfo)
    local_time = gmt_time.astimezone(local_tzinfo)
    if time == 0 :
        return local_time.strftime("%Y-%m-%d")  
    else :
        return local_time.strftime("%Y-%m-%d %H:%M:%S") 

def check_time(da):
    to_tzinfo =    GMT()#格林威治时区，0时区
    local_tzinfo =  GMT8()#本地时区，+8区
    gmt_time = datetime.datetime.strptime(da, '%Y-%m-%d %H:%M:%S')
    gmt_time = gmt_time.replace(tzinfo=local_tzinfo)
    local_time = gmt_time.astimezone(to_tzinfo)

    return  int(time.mktime(datetime.datetime.utcnow().utctimetuple()) - time.mktime(local_time.timetuple()))  


