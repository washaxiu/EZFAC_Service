#!/usr/bin/env python
# -*- coding:UTF-8 -*-

__author__ = 'Spring'
__date__ = '18-4-30'
__time__ = '11:05'
__description__ = 'HomeHandler'

import tornado.web
import tornado.gen
import os.path
import tcelery
from task import *
import json
from common.log import *
from web.auth_handle import *
from web.handle.HomeHandler import BaseHandler


"""
    Device ykk Handler
"""

class GetMaintenanceLogHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        resp = yield tornado.gen.Task(task.get_maintenanceLog_task.apply_async, args=[])
        resp_json = json.dumps(resp.result)
        self.write(resp_json)

class GetSemiFinishedCheckHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        resp = yield tornado.gen.Task(task.get_semiFinishedCheck_task.apply_async, args=[])
        resp_json = json.dumps(resp.result)
        self.write(resp_json)

class GetYZGCMonthRecordHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        resp = yield tornado.gen.Task(task.get_YZGCMonthRecord_task.apply_async, args=[])
        resp_json = json.dumps(resp.result)
        self.write(resp_json)