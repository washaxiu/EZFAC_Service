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
		table_name = self.get_argument("table_name")
        resp = yield tornado.gen.Task(task.get_checkRecord_list_task.apply_async, args=[table_name])
        resp_json = json.dumps(resp.result)
        self.write(resp_json)

#class AddCheckRecordHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
          fileName = self.get_argument("fileName")
          type = self.get_argument("type")
          group1 = self.get_argument("group")
          number = self.get_argument("number")
          temp1 = self.get_argument("Temp1")
          temp2 = self.get_argument("Temp2")
          temp3 = self.get_argument("Temp3")
          loop1 = self.get_argument("Loop1")
          loop2 = self.get_argument("Loop2")
          loop3 = self.get_argument("Loop3")
          select1 = self.get_argument("Select1")
          plat1 = self.get_argument("Plat1")
          checkEdit = self.get_argument("checkEdit")
          name1 = self.get_argument("name1")
          name2 = self.get_argument("name2")
          name3 = self.get_argument("name3")
          name4 = self.get_argument("name4")
          name5 = self.get_argument("name5")
          date1 = self.get_argument("date1")
          date2 = self.get_argument("date2")
          date3 = self.get_argument("date3")
          date4 = self.get_argument("date4")
          date5 = self.get_argument("date5")
          comments1 = self.get_argument("comments1")
          comments2 = self.get_argument("comments2")
          comments3 = self.get_argument("comments3")
          comments4 = self.get_argument("comments4")
          comments5 = self.get_argument("comments5")
          checkerEdit = self.get_argument("checkerEdit")
          check = self.get_argument("check")
          level = self.get_argument("level")
		  checkRecord = {"fileName":fileName,"type":type,"group1":group1,"number":number,"temp1":temp1,
		                "temp2":temp2,"temp3":temp3,"loop1":loop1,"loop2":loop2,"loop3":loop3,
						"select1":select1,"select1":select1,"edit":checkEdit}
          resp = yield tornado.gen.Task(task.add_checkRecord_task.apply_async, args=[checkRecord])
          return self.render("device.html")