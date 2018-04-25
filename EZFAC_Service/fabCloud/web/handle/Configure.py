#!/usr/bin/env python
# -*- coding:UTF-8 -*-

__author__ = 'AvyGong'
__date__ = '15-7-3'
__time__ = '17:30'
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
    Device configure Handler
"""
class DeviceListGetHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        resp = yield tornado.gen.Task(task.get_device_list_task.apply_async, args=[])
        devices = resp.result
        respData = json.dumps(devices)
        self.write(respData)


class DeviceTypesGetHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        resp = yield tornado.gen.Task(task.get_device_type_list_task.apply_async, args=[])
        devtypes = resp.result
        respData = json.dumps(devtypes)
        self.write(respData)


class DeleteDeviceHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        devid = int(self.get_argument("device_id"))
        delkey = {"id": devid}
        resp = yield tornado.gen.Task(task.delete_device_task.apply_async, args=[delkey])
        return self.render("device.html")


class DeviceConfigureHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        action = self.get_argument("action")
        device_name = self.get_argument("device_name")
        equipment_id = self.get_argument("equipment_id")
        device_type_id = self.get_argument("device_type")
        description = self.get_argument("description")
        alarm_threshold = self.get_argument("alarm_threshold")
        contact_group_id = int(self.get_argument("notify_group"))
        device_enable = int(self.get_argument("device_enable"))
        dev_cfg = {"device_name": device_name, "equipment_id": equipment_id, "device_type_id": device_type_id, 
            	"threshold": alarm_threshold, "enable": device_enable, "description":description,
            	"contact_group_id":contact_group_id}
        if action == "add":           
            resp = yield tornado.gen.Task(task.add_device_task.apply_async, args=[dev_cfg])
            return self.render("device.html")
        else:
            devid = int(self.get_argument("device_id"))
            resp = yield tornado.gen.Task(task.edit_device_task.apply_async, args=[devid, dev_cfg])
            self.render("device.html")


"""
    Line configure Handler
"""
class GetLineTypeListHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        resp = yield tornado.gen.Task(task.get_line_type_task.apply_async, args=[])
        resp_json = json.dumps(resp.result)
        self.write(resp_json)


class GetLineListHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        resp = yield tornado.gen.Task(task.get_line_task.apply_async, args=[])
        resp_json = json.dumps(resp.result)
        self.write(resp_json)

class GetLineStatusHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        resp = yield tornado.gen.Task(task.get_line_status_task.apply_async, args=[])
        resp_json = json.dumps(resp.result)
        self.write(resp_json)

class AddLineHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        line_type = self.get_argument("line_type")
        line_name = self.get_argument("line_name")
        line_description = self.get_argument("line_description")
        if self.get_argument("Timeout"):
            Timeout = int(self.get_argument("Timeout"))
        else:
            Timeout = 0
        if self.get_argument("worktime"):
            worktime = int(self.get_argument("worktime"))
        else:
            worktime = 0
        enable = self.get_argument("enable")
        contact_group_id = int(self.get_argument("notify_group"))
        Threshold=self.get_argument("Threshold")
        linecfg = {'line_type_id': line_type, 'line_name': line_name,
                    'description': line_description, 'timeout': Timeout,'worktime':worktime,
                    'threshold': Threshold,'enable': int(enable), "contact_group_id":contact_group_id}
        resp = yield tornado.gen.Task(task.add_line_cfg_task.apply_async, args=[linecfg])
        if resp.result == True:
            back_info = [{'add': 1}]
        else:
            back_info = [{'add': 0}]
        respJson = json.dumps(back_info)
        self.write(respJson)


class SetEditLineHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        line_id = self.get_argument("line_id")
        line_type = self.get_argument("line_type")
        line_name = self.get_argument("line_name")
        line_description = self.get_argument("line_description")
        if self.get_argument("Timeout"):
            Timeout = int(self.get_argument("Timeout"))
        else:
            Timeout = 0
        if self.get_argument("worktime"):
            worktime = int(self.get_argument("worktime"))
        else:
            worktime = 0
        enable = self.get_argument("enable")
        contact_group_id = int(self.get_argument("notify_group"))
        Threshold=self.get_argument("Threshold")
        linecfg = {'line_type_id': line_type, 'line_name': line_name,'id': int(line_id),
                    'description': line_description, 'timeout': Timeout,'worktime': worktime,
                    'threshold': Threshold,'enable': int(enable), "contact_group_id":contact_group_id}
        resp = yield tornado.gen.Task(task.edit_line_cfg_task.apply_async, args=[linecfg])
        if resp.result=='error':
            back_info = [{'add': 0}]
        else:
            back_info = [{'add': 1}]
        respJson = json.dumps(back_info)
        self.write(respJson)


class DeleteLineHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        line_id = self.get_argument("line_id")
        resp = yield tornado.gen.Task(task.delete_line_cfg_task.apply_async, args=[line_id])
        self.render("line.html")


class RefrashLineHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        line_id = self.get_argument("line_id")
        resp = yield tornado.gen.Task(task.refrash_line_tassk.apply_async, args=[line_id])
        if resp.result==True:
            back_info = [{'refrash': 1}]
        else:
            back_info = [{'refrash': 0}]
        respJson = json.dumps(back_info)
        self.write(respJson)

class AddLineOrDeviceTypeHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        add_type = self.get_argument("add_type")
        type_name = self.get_argument("type_name")
        type_description = self.get_argument("type_description")
        worktime = self.get_argument("worktime")
        upload_path = os.path.join(os.path.dirname(__file__), '../static/device_image/')
        file_metas = self.request.files['type_image']
        for meta in file_metas:
            filename = meta['filename']
            filepath = os.path.join(upload_path, filename)
            with open(filepath, 'wb') as up:
                up.write(meta['body'])
        linetpyecfg = {'add_type': add_type,'type_name':type_name, 'type_image':filename, 'type_description':type_description, 'worktime':worktime}
        resp = yield tornado.gen.Task(task.add_line_device_type_task.apply_async, args=[linetpyecfg])
        self.render("misc.html")
        
        
class DelLineOrDeviceTypeHandler(BaseHandler):
    @BaseHandler.auth
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        del_type = self.get_argument("del_type")
        type_id = int(self.get_argument("type_id"))
        resp = yield tornado.gen.Task(task.delete_line_device_type_task.apply_async, args=[del_type, type_id])
        self.render("misc.html")
