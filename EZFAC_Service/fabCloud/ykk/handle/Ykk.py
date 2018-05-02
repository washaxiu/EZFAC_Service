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
from ykk.auth_handle import *
from ykk.handle.HomeHandler import BaseHandler


"""
    Device ykk Handler
"""

class GetCheckRecordListHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        resp = yield tornado.gen.Task(task.get_checkRecord_list_task.apply_async, args=[])
        resp_json = json.dumps(resp.result)
        self.write(resp_json)

#class AddCheckRecordHandler(BaseHandler):
#	@BaseHandler.auth
#	@tornado.web.asynchronous
#	@tornado.gen.coroutine
#	def post(self, *args, **kwargs):
        # devid = int(self.get_argument("device_id"))
        # delkey = {"id": devid}
        # resp = yield tornado.gen.Task(task.delete_device_task.apply_async, args=[delkey])
        # return self.render("device.html")