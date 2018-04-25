#!/usr/bin/env python
# -*- coding:UTF-8 -*-

__author__ = 'avy'
__date__ = '15-1-10'
__time__ = '9:16'
__description__ = 'url map'

from web.handle.HomeHandler import *
from web.handle.Management import *
from web.handle.Configure import *
from web.handle.Monitor import *
from web.handle.Dashboard import *

URLS = [
    (r"/", HomeHandler),
    (r"/restore.html", BackupRestorePageHandler),
    (r"/(.*).html", PageHandler),    
    # configure device
    (r"/device_configure", DeviceConfigureHandler),
    (r"/deviceListGet", DeviceListGetHandler),
    (r"/deviceTypesGet", DeviceTypesGetHandler),
    (r"/delete_device", DeleteDeviceHandler),
    # configure line
    (r"/get-line-type-list", GetLineTypeListHandler),
    (r"/get-line-list", GetLineListHandler),
    (r"/get-line-status", GetLineStatusHandler),
    (r"/add-line", AddLineHandler),
    (r"/set-edit-line", SetEditLineHandler),
    (r"/delete-line", DeleteLineHandler),
    (r"/refrash-line", RefrashLineHandler),
    (r"/add-type", AddLineOrDeviceTypeHandler),
    (r"/delete_type", DelLineOrDeviceTypeHandler),
    # management user
    (r"/user_login", UserLoginHandler),
    (r"/add-user", AddUserHandler),
    (r"/edit-user", EditUserHandler),
    (r"/get-group-user-info", GetGroupUserInfoHandler),
    (r"/get-current-groupId", GetUserGroupIdHandler),
    (r"/delete-user-name", DeleteUserHandler),
    (r"/get-contact-list", GetContactListHandler),
    (r"/contact_configure", ContactConfigureHandler),
    (r"/delete_contact", DeleteContactHandler),
    (r"/get-contact-group-list", GetContactGroupHandler),
    (r"/contact_group_configure", ContactGroupConfigHandler),
    (r"/get-contact2group-map", GetGroupContactMapHandler),
    (r"/backup_restore", DatabaseBackupRestoreHandler),
    # monitor
    (r"/get-lineDevice-location", GetLineDeviceLocationHandler),
    (r"/get-line-pass-status", GetLinePassStatusHandler),
    (r"/get-device-status", GetDeviceStatusHandler),
    (r"/get-alarm-info", GetAlarmHandler),
    (r"/get-user-radio", GetRadioHandler),

]
