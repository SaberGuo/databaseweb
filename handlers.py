#!/usr/bin/env python
#coding=utf-8

import tornado.ioloop

import tornado.web
import models
import timehelper
import time

class Mainhandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('main.html')

class Datahandler(tornado.web.RequestHandler):
    def get(self):
        return self.render('data.html')

class Taskhandler(tornado.web.RequestHandler):
    def get(self, flag=''):
        warning=flag
        tasks=models.task.find_all()
        unfinished_tasks=[]
        finished_tasks=[]
        if tasks:
            for x in tasks:
                if x['start_time']==None or x['end_time']==None:
                    unfinished_tasks.append(x)
                else:
                    finished_tasks.append(x)
        return self.render('task.html',warning=warning, unfinished_tasks=unfinished_tasks, finished_tasks=finished_tasks)

    def post(self):
        warning=''
        if self.get_argument('isdelete')=='True':
            taskname=self.get_argument('taskname')
            task=models.task.find_first('where taskname=?', taskname)
            task.delete()
            self.get(warning)
        else:
            if models.task.count_by('where start_time=?', False):
                warning='There is an unfinished task!'
            else:
                taskname=self.get_argument('taskname','')
                attribute=self.get_argument('attribute','')
                explanation=self.get_argument('explanation','')
                profile=self.get_argument('profile')
                if profile==u'遥测数据':
                    profile='telemetry_data'
                elif profile==u'回复数据':
                    profile='response_data'
                elif profile==u'命令数据':
                    profile='command_data'
                if taskname:
                    task=models.task.find_by('where taskname=?', taskname)
                    if not task:
                        task=models.task(id=timehelper.next_id(), taskname=taskname, attribute=attribute, explanation=explanation,
                        	 start_time='None', end_time='None', profile=profile)
                        task.insert()
                    else:
                        warning='Same taskname!'
                else:
                    warning='Empty taskname!'
        self.get(warning)

class Task_starthandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        data=self.get_argument('startingtask')
        self.get_data(data=data, callback=self.on_finish)
             
    def get_data(self, data, callback):
        if self.request.connection.stream.closed():
            return
        raw_data=models.raw_data.find_first('where task_id=?', data)
        tornado.ioloop.IOLoop.instance().add_timeout(
            time.time()+0.1,
            lambda: callback(raw_data['id'])
        ) 
             
    def on_finish(self, data):
        self.write(data)
        self.finish() 

class Task_timehandler(tornado.web.RequestHandler):
    def post(self):
        if self.get_argument('flag')=='0':
            data=self.get_argument('startingtask')
            task=models.task.find_first('where taskname=?', data)
            task.start_time=timehelper.createtime()
            task.delete()
            task.insert()
            return
        if self.get_argument('flag')=='1':
            data=self.get_argument('startingtask')
            task=models.task.find_first('where taskname=?', data)
            task.end_time=timehelper.createtime()
            task.delete()
            task.insert()
            return