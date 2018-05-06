#!/usr/bin/env python
# -*- coding:UTF-8 -*-

__author__ = 'avy'
__date__ = '15-1-10'
__time__ = '9:16'
__description__ = 'url map'

from ykk.handle.HomeHandler import *
from ykk.handle.Management import *
from ykk.handle.Configure import *
from ykk.handle.Monitor import *
from ykk.handle.Dashboard import *
from ykk.handle.Ykk import *

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
    # ykk
    (r"/get-userInfo", GetUserInfoHandler),
    (r"/get-checkRecord-list", GetCheckRecordListHandler),
    (r"/add-checkRecord", AddCheckRecordHandler),
    (r"/add-DailyCheckMorning", AddDailyCheckMorningHandler),
    (r"/add-DailyCheckNoon", AddDailyCheckNoonHandler),
    (r"/add-MaintenanceLog", AddMaintenanceLogHandler),

]
