#!/usr/bin/env python
#coding=utf-8

import tornado.ioloop
import tornado.web
import db
import random
import models
import os
import time
import timehelper

# class LongPollingHandler(tornado.web.RequestHandler):
#     @tornado.web.asynchronous
#     def post(self):
#         self.get_data(callback=self.on_finish)
             
#     def get_data(self, callback):
#         if self.request.connection.stream.closed():
#             return
             
#         num = random.randint(1, 100)
#         tornado.ioloop.IOLoop.instance().add_timeout(
#             time.time()+3,
#             lambda: callback(num)
#         ) # 间隔3秒调用回调函数
             
#     def on_finish(self, data):
#         self.write("Server says: %d" % data)
#         self.finish() # 使用finish方法断开连接
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         return self.render('test.html')
# settings={
#     'static_path':os.path.join(os.path.dirname(__file__),'static'),
#     'template_path':os.path.join(os.path.dirname(__file__),'templates'),
#     'debug':True
# }

# application=tornado.web.Application([
# 	(r"/",MainHandler),
# 	(r"/longpolling",LongPollingHandler)
# 	],**settings)
# application.listen(8080)
# tornado.ioloop.IOLoop.instance().start()
db.create_engine('yjc','','databaseweb')
task=models.task.find_first('where taskname=?', '1')
task.start_time=timehelper.createtime()
task.delete()
task.insert()