#!/usr/bin/env python
#coding=utf-8

from orm import Model, StringField, BlobField, IntegerField, TextField
from timehelper import createtime, next_id

class user(Model):
    __table__='user'

    id=StringField(primary_key=True, default=next_id, updatable=False, ddl='varchar(50)')
    username=StringField(ddl='varchar(20)')

class task(Model):
    __table__='task'

    id=StringField(primary_key=True, default=next_id, ddl='varchar(50)', updatable=False)
    taskname=StringField(ddl='varchar(20)')
    attribute=StringField(ddl='varchar(20)')
    explanation=StringField(ddl='varchar(255)')
    start_time=StringField(updatable=False, default=createtime)
    end_time=StringField(updatable=False, default=createtime)
    profile=TextField()

class raw_data(Model):
    __table__='raw_data'

    id=StringField(primary_key=True, default=next_id, updatable=False, ddl='varchar(50)')
    task_id=StringField(ddl='varchar(50)',updatable=False)
    value=BlobField()
    time=StringField(ddl='varchar(50)', updatable=False, default=createtime)

class telemetry_data(Model):
    __table__='telemetry_data'

    id=StringField(primary_key=True, updatable=False, ddl='varchar(50)', default=next_id)
    task_id=StringField(updatable=False, ddl='varchar(50)')
    raw_data_id=StringField(updatable=False, ddl='varchar(50)')
    nameID=StringField(ddl='varchar(20)')
    valuetype=StringField(ddl='varchar(20)')
    value=StringField()
    unit=StringField(ddl='varchar(20)')
    time=StringField(ddl='varchar(50)', updatable=False, default=createtime)

class response_data(Model):
    __table__='response_data'

    id=StringField(primary_key=True, updatable=False, ddl='varchar(50)', default=next_id)
    task_id=StringField(updatable=False, ddl='varchar(50)')
    raw_data_id=StringField(updatable=False, ddl='varchar(50)')
    nameID=StringField(ddl='varchar(20)')
    valuetype=StringField(ddl='varchar(20)')
    value=StringField()
    unit=StringField(ddl='varchar(20)')
    time=StringField(ddl='varchar(50)', updatable=False, default=createtime)

class comman_data(Model):
    __table__='command_data'

    id=StringField(primary_key=True, updatable=False, ddl='varchar(50)', default=next_id)
    task_id=StringField(updatable=False, ddl='varchar(50)')
    raw_data_id=StringField(updatable=False, ddl='varchar(50)')
    nameID=StringField(ddl='varchar(20)')
    valuetype=StringField(ddl='varchar(20)')
    value=StringField()
    unit=StringField(ddl='varchar(20)')
    time=StringField(ddl='varchar(50)', updatable=False, default=createtime)
