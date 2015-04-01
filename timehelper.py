#!/usr/bin/env python
#coding=utf-8
import time, uuid

def next_id():
    return '%015d%s000' % (int(time.time()*1000), uuid.uuid4().hex)

def createtime():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())