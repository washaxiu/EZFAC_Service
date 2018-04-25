__author__ = 'AvyGong'


import task.util
from task.util import *
import os

"""
    Device configure task
"""
@app.task
@use_db
def get_device_list_task():
    devices = db.query_all("device_config")
    if devices:
        return devices
    else:
        return None


@app.task
@use_db
def get_device_type_list_task():
    devType = db.query_all("device_type")
    ret = []
    if devType:
        for dtype in devType:
            leType_dict = {}
            leType_dict['id'] = dtype['id']
            leType_dict['device_type'] = dtype['device_type']
            leType_dict['description'] = dtype['description']
            filename = "device_" + str(dtype['device_type'])+str(dtype['id']) +".jpg"
            linefile = "web/static/device_image/" + filename
            fout = open(linefile,'wb+')
            fout.write(dtype['icon'])
            leType_dict['icon']=filename
            ret.append(leType_dict)
    return ret


@app.task
@use_db
def add_device_task(cfg):
    ret = db.insert("device_config", cfg)
    return ret


@app.task
@use_db
def edit_device_task(devid,cfg):
    ret = db.update("device_config", cfg, {"id":devid})
    return ret


@app.task
@use_db
def delete_device_task(cfg):
    ret = db.delete("device_config", cfg)
    return ret


"""
    Line configure task
"""
@app.task
@use_db
def get_line_type_task():
    le_type_list = []
    le_types = db.query_all("line_type")
    if le_types:
        for le_type in le_types:
            leType_dict = {}
            leType_dict['line_type_id'] = le_type['id']
            leType_dict['line_type_name'] = le_type['line_type']
            leType_dict['line_description'] = le_type['description']
            leType_dict['worktime'] = le_type['worktime']
            filename = "line_" + str(le_type['line_type'])+str(le_type['id']) +".jpg"
            linefile = "web/static/device_image/" + filename
            fout = open(linefile,'wb+')
            fout.write(le_type['icon'])
            leType_dict['icon']=filename
            le_type_list.append(leType_dict)
    if len(le_type_list) != 0:
        return le_type_list
    else:
        return None


@app.task
@use_db
def get_line_task():
    line_list_dicts = []
    line_lists = db.query_all("line_config")
    if line_lists:
        for line_list in line_lists:
            line_dict = {}
            line_dict['id'] = line_list['id']
            line_dict['line_name'] = line_list['line_name']
            line_dict['line_type_id'] = line_list['line_type_id']
            line_dict['current_status'] = line_list['current_status']
            line_dict['description'] = line_list['description']
            line_dict['enable'] = line_list['enable']
            line_dict['threshold'] = line_list['threshold']
            line_dict['timeout'] = line_list['timeout']
            line_dict['worktime'] = line_list['worktime']
            line_list_dicts.append(line_dict)
    if len(line_list_dicts) != 0:
        return line_list_dicts
    else:
        return None


@app.task
@use_db
def get_line_status_task():
    line_list_dicts = []
    line_lists = db.query_all("line_config")
    recover_times = 0
    error_times = 0
    alarm_times = 0
    offline_times = 0
    if line_lists:
        for line_list in line_lists:
            line_dict = {}
            line_dict['id'] = line_list['id']
            line_dict['line_name'] = line_list['line_name']
            line_dict['current_status'] = line_list['current_status']
            line_dict['description'] = line_list['description']
            line_dict['enable'] = line_list['enable']
            date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            use_ratio = db.query_one("line_usage_ratio", {"line_id":line_list['id'], "date":date})
            if use_ratio:
                line_dict['usage_ratio'] = use_ratio['usage_ratio']
            else:
                line_dict['usage_ratio'] = 0
            line_status = db.query("line_day_status", {"line_id":line_list['id']})
            if line_status:
                for line in line_status:
                    edate = str(line['start_time'])
                    tmp = edate.split(' ')
                    if date == tmp[0]:
                        state = line['status']
                        if state == 'G':
                            recover_times += 1
                        elif state == 'R':
                            error_times += 1
                        elif state == 'Y':
                            alarm_times += 1
                        else:
                            offline_times += 1
            line_dict['recover_times'] = recover_times
            line_dict['error_times'] = error_times
            line_dict['alarm_times'] = alarm_times
            line_dict['offline_times'] = offline_times
            line_list_dicts.append(line_dict)
        return line_list_dicts
    else:
        return None


@app.task
@use_db
def add_line_cfg_task(cfg):
    ret = False
    if len(cfg) != 0:
        ret = db.insert("line_config", {'line_type_id': cfg['line_type_id'], 'line_name': cfg['line_name'],
                                        'description': cfg['description'], 'timeout': cfg['timeout'],
                                        'worktime': cfg['worktime'], 'threshold': cfg['threshold'],
                                        'enable': cfg['enable']})
    return ret


@app.task
@use_db
def edit_line_cfg_task(cfg):
    ret = False
    if len(cfg) != 0:
        edit_user_cfg = db.query_one("line_config", {'line_name': cfg['line_name']})
        if edit_user_cfg and edit_user_cfg['id']!= cfg['id']:
            return 'error'
        ret = db.update("line_config", {'line_type_id': cfg['line_type_id'], 'line_name': cfg['line_name'],
                                        'description': cfg['description'], 'timeout': cfg['timeout'],
                                        'worktime': cfg['worktime'], 'threshold': cfg['threshold'],
                                        'enable': cfg['enable']}, {'id': cfg['id']})
    return ret


@app.task
@use_db
def delete_line_cfg_task(line_id):
    ret = False
    if len(line_id) != 0:
        ret = db.delete("line_config", {"id": line_id}, True)
    return ret


@app.task
@use_db
def refrash_line_tassk(line_id):
    ret = False
    if len(line_id) != 0:
        ret = db.delete("line2device", {"line_id": line_id}, True)
    return ret


@app.task
@use_db
def add_line_device_type_task(cfg):
    if cfg['add_type']=='L':
        mapfile = "web/static/device_image/" + cfg['type_image']
        fd = open(mapfile,'rb')
        map_image = fd.read()
        ret = db.insert("line_type",{'line_type':cfg['type_name'],'description':cfg['type_description'],'worktime':cfg['worktime'],'icon':map_image} )
    else:
        mapfile = "web/static/device_image/" + cfg['type_image']
        fd = open(mapfile,'rb')
        map_image = fd.read()
        ret = db.insert("device_type",{'device_type':cfg['type_name'],'description':cfg['type_description'],'icon':map_image} )
    return ret


@app.task
@use_db
def delete_line_device_type_task(del_type, type_id):
    if del_type == "line":
        ret = db.delete("line_type", {"id":type_id})
    else:
        ret = db.delete("device_type", {"id":type_id})
    return ret    	
