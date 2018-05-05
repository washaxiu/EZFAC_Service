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

class GetUserInfoHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        resp = yield tornado.gen.Task(task.get_userInfo_task.apply_async, args=[])
        resp_json = json.dumps(resp.result)
        self.write(resp_json)

class GetCheckRecordListHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        table_name = self.get_argument("table_name")
        level = self.get_argument("level")
        cfg = {"table_name":table_name,"level":level}
        resp = yield tornado.gen.Task(task.get_checkRecord_list_task.apply_async, args=[cfg])
        resp_json = json.dumps(resp.result)
        self.write(resp_json)

class AddCheckRecordHandler(BaseHandler):
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
			 "select1":select1,"plat1":plat1,"edit":checkEdit}
          checkerInfo = {"fileName":fileName,"name1":name1,"name2":name2,"name3":name3,"name4":name4,
		         "name5":name5,"date1":date1,"date2":date2,"date3":date3,"date4":date4,
			 "date5":date5,"comments1":comments1,"comments2":comments2,"comments3":comments3,
			 "comments4":comments4,"comments5":comments5,"edit":checkerEdit,
			 "isCheck":check,"level":level}
          respCheck = yield tornado.gen.Task(task.add_checkRecord_task.apply_async, args=[checkRecord])
          respChecker = yield tornado.gen.Task(task.add_checkerInfo_task.apply_async, args=[checkerInfo])
          if respCheck.result == True and respChecker.result == True:
            back_info = 1
          else:
            back_info = 0
          respJson = json.dumps(back_info)
          self.write(respJson)
