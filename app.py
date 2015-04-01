#!/usr/bin/env python
#coding=utf-8

import os
import tornado.web
import tornado.ioloop
from handlers import *
import db

handlers=[
    (r'/',Mainhandler),
    (r'/task',Taskhandler),
    (r'/data',Datahandler),
    (r'/task_start',Task_starthandler),
    (r'/tasktime', Tasktimehandler)
]

settings={
    'static_path':os.path.join(os.path.dirname(__file__),'static'),
    'template_path':os.path.join(os.path.dirname(__file__),'templates'),
    'debug':True
}

app=tornado.web.Application(handlers, **settings)
app.listen(8080)
db.create_engine('yjc','','databaseweb')
tornado.ioloop.IOLoop.instance().start()